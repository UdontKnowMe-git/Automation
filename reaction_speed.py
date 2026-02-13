from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import pyautogui as pg
import time


browser = webdriver.Chrome()
browser.start_client()
browser.maximize_window()
browser.get("https://humanbenchmark.com/tests/reactiontime")


wait = WebDriverWait(browser, 10)
initial_screen = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "view-splash")))
initial_screen.click()

# class name when item is waiting to be clicked
waitClass = "view-waiting css-1s9j8qg"

# class name when item is ready to be clicked
searchClass = "view-go css-yg2dtu"

# class name when successfully clicked
successClass = "view-result css-yg2dtu"

for i in range(5):
    # 1. Wait specifically for the green "GO" screen
    target = WebDriverWait(browser, 20, poll_frequency=0.001).until(
        EC.presence_of_element_located((By.CLASS_NAME, "view-go"))
    )
    
    # 2. Click immediately
    target.click()
    
    # 3. Wait for the result screen and click it to reset for the next round
    next_round = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "view-result")))
    next_round.click()
    