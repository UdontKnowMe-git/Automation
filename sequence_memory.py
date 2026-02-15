import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://humanbenchmark.com/tests/sequence")
browser.maximize_window()

time.sleep(2)  # Wait for the page to load
#  Start the game
start_button = browser.find_element(By.CLASS_NAME, "css-1bnidmp")
start_button.click()

# Inject a "Watcher" script into the browser
# This script sits inside the page and records the order of flashes
watcher_script = """
window.sequence = [];
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.target.classList.contains('active')) {
            // Get the index of the square (0-8)
            const squares = Array.from(document.querySelectorAll('.square'));
            const index = squares.indexOf(mutation.target);
            // Only add if it's the start of the flash
            if (!window.sequence.length || window.sequence[window.sequence.length - 1] !== index) {
                window.sequence.push(index);
            }
        }
    });
});

const grid = document.querySelector('.squares');
observer.observe(grid, { attributes: true, subtree: true, attributeFilter: ['class'] });
"""
browser.execute_script(watcher_script)

def solve_level():
    wait = WebDriverWait(browser, 10)
    
    try:
        # 1. Wait for the parent span to appear
        parent_span = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-4rar09")))
        
        # 2. Get the actual level number from the SECOND child span
        # This is more reliable than splitting strings
        level_text = ""
        for _ in range(20):
            try:
                # Find the span that specifically contains the number
                level_text = parent_span.find_elements(By.TAG_NAME, "span")[1].text
                if level_text.isdigit():
                    break
            except IndexError:
                pass # The second span hasn't rendered yet
            time.sleep(0.1)
            
        if not level_text:
            return False

        level = int(level_text)
        print(f"Watching Level {level}...")
        
    except Exception as e:
        print(f"Error finding level: {e}")
        return False

    # --- Reset JS and watch for flashes ---
    browser.execute_script("window.sequence = [];")

    captured_seq = []
    while len(captured_seq) < level:
        captured_seq = browser.execute_script("return window.sequence;")
        time.sleep(0.05)
    
    # Wait for the light to turn off on the last square
    time.sleep(0.5)

    # --- Perform the clicks ---
    squares = browser.find_elements(By.CLASS_NAME, "square")
    for index in captured_seq:
        squares[index].click()
        time.sleep(0.05)
    
    return True

current_level = 0

while True:
    wait = WebDriverWait(browser, 10)
    try:
        # This waits until the level number is strictly greater than the one we just finished
        wait.until(lambda d: int(d.find_element(By.CLASS_NAME, "css-4rar09").find_elements(By.TAG_NAME, "span")[1].text) > current_level)
    except Exception as e:
        print("Game over or timed out waiting for next level.")
        break
    if not solve_level():
        break
    current_level += 1
    
    time.sleep(0.5)