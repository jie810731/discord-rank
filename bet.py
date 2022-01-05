
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pause
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import random

def web_driver_init(): 
    options = Options()

    # options.add_argument('--headless')
    options.add_argument("window-size=1440,1900")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('–incognito')
    options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    mobile_emulation = {
        "deviceMetrics": { "width": 400, "height": 156, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)


    driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromedriver', chrome_options=options)

    return driver

def login():
    driver.get("https://discord.com/login")
    element = driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To inputField-4g7rSQ']")
    element.send_keys('帳號')

    element = driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To']")
    element.send_keys('密碼')

    driver.find_element_by_xpath("//button[@class='marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN']").click()

    

def getToken():
    target = 'https://discord.com/channels/@me'
    wait = True
    while wait:
        if driver.current_url == 'https://discord.com/channels/@me' :
            wait = False
    
    storage = driver.execute_script("var iframe = document.createElement('iframe'); iframe.onload = function(){ var ifrLocalStorage = iframe.contentWindow.localStorage;}; iframe.src = 'about:blank'; document.body.appendChild(iframe); return iframe.contentWindow.localStorage.getItem('token');")
    print(storage)
    

def gotoChannel():
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='sidebar-2K8pFh hasNotice-1XRy4h']")))
    driver.get("https://discord.com/channels/902273042795864085/919045018222735380")

def playGame():
    xpath = "//div[@class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']"
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, xpath))
    )
    element = driver.find_element_by_xpath(xpath)

    element.send_keys('L.slot 100')
    element.send_keys(Keys.ENTER)

    # start_button_x_path = "//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN']"
    start_button_x_path = "//div[@class='label-3aEGGA']  | //div[contains(text(),'Start')]"

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, start_button_x_path))
    )
    time.sleep(3)
    element = driver.find_element_by_xpath(start_button_x_path).click()

try:
    driver  = web_driver_init()
    login()
    getToken()
    # gotoChannel()
    # playGame()

    

    # time.sleep(50)

except Exception as e:
    # print('aa')
    print(e)
    driver.quit()

driver.quit()