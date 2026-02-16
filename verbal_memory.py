import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://humanbenchmark.com/tests/verbal-memory")
browser.maximize_window()

time.sleep(2)  # Wait for the page to load
#  Start the game
start_button = browser.find_element(By.CLASS_NAME, "css-1bnidmp")
start_button.click()

word_set = set()

def find_word():
    wait = WebDriverWait(browser, 10)
    
    try:
        word_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "word")))
        word = word_element.text.strip()
        return word
    except:
        return None
    
while True:
    word = find_word()
    if not word:
        break
    
    if word in word_set:
        # Using XPATH for clarity
        browser.find_element(By.XPATH, "//button[text()='SEEN']").click()
    else:
        word_set.add(word)
        browser.find_element(By.XPATH, "//button[text()='NEW']").click()

    time.sleep(0.05)