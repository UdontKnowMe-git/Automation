from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.start_client()
browser.maximize_window()
browser.get("https://humanbenchmark.com/tests/sequence")

wait = WebDriverWait(browser, 10)
initial_screen = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1bnidmp")))
initial_screen.click()

searchClass = "square active"

sequence = []
