from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, \
    NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver import Keys
import random
import time
import datetime
from dotenv import dotenv_values
import pandas as pd

ENV = dotenv_values("../.env")
start_time = time.time()
now = datetime.datetime.now()
firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.set_preference("browser.download.folderList", 2)
firefoxOptions.set_preference("browser.download.useDownloadDir", True)
firefoxOptions.set_preference("browser.download.viewableInternally.enabledTypes", "")
firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
firefoxOptions.set_preference("browser.download.dir", ENV.get("UPLOAD_AND_DOWNLOAD_PATH"))
firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip;application/pdf;text/plain;application/text;text/xml;application/xml")
firefoxOptions.set_preference("pdfjs.disabled", True)
if ENV.get("DISABLE_SHOW_UI") == "true":
    firefoxOptions.add_argument("-headless")
driver = webdriver.Firefox(options=firefoxOptions)
driver.maximize_window()
driver.implicitly_wait(30)
