from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, \
    NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import random
import time
import datetime
from dotenv import dotenv_values
import pandas as pd

ENV = dotenv_values("../.env")
start_time = time.time()
now = datetime.datetime.now()
chromeOptions = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": ENV.get("UPLOAD_AND_DOWNLOAD_PATH"),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
CHROMEDRIVER_PATH = ENV.get("CHROMEDRIVER_PATH")
chromeOptions.add_experimental_option("prefs", prefs)
if ENV.get("DISABLE_SHOW_UI") == "true":
    chromeOptions.add_argument("-headless")
service = webdriver.ChromeService(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeOptions)
driver = webdriver.Chrome(options=chromeOptions, service=service)
driver.maximize_window()
driver.implicitly_wait(30)
