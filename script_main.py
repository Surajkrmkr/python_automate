import xpath_miui
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import data
import time


mtzList = []

for (root, dirs, file) in os.walk(data.path):
    for f in file:
        if '.mtz' in f:
            mtzList.append(f)


options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
options.add_experimental_option('excludeSwitches', ['enable-logging'])
webBrowser = webdriver.Chrome(
    executable_path=r"chromedriver.exe", options=options)
webBrowser.maximize_window()

homeUrl = "https://in.zhuti.designer.intl.xiaomi.com/"

webBrowser.get(homeUrl)


wait = WebDriverWait(webBrowser, 300)
wait.until(EC.presence_of_element_located(
    (By.XPATH, xpath_miui.signIn)))
webBrowser.find_element(By.XPATH, xpath_miui.signIn).click()
# wait.until(EC.presence_of_element_located(
#     (By.XPATH, xpath_miui.signInUsingPw)))
# webBrowser.find_element(By.XPATH, xpath_miui.signInUsingPw).click()
wait.until(EC.presence_of_element_located((By.XPATH, xpath_miui.emailId)))
webBrowser.find_element(By.XPATH, xpath_miui.emailId).send_keys("8637258912")
wait.until(EC.presence_of_element_located((By.NAME, xpath_miui.pw)))
webBrowser.find_element(By.NAME, xpath_miui.pw).send_keys("suraj123")
wait.until(EC.presence_of_element_located((By.XPATH, xpath_miui.submit)))
webBrowser.find_element(By.XPATH, xpath_miui.submit).click()
wait.until(EC.presence_of_element_located((By.XPATH, xpath_miui.cookieBtn)))
webBrowser.find_element(By.XPATH, xpath_miui.cookieBtn).click()
wait.until(EC.presence_of_element_located((By.XPATH, xpath_miui.dialogOkBtn)))
webBrowser.find_element(By.XPATH, xpath_miui.dialogOkBtn).click()
mainWindow = webBrowser.current_window_handle

for i in range(len(mtzList)):
    webBrowser.execute_script("window.open('about:blank',"+str(i)+");")
    webBrowser.switch_to.window(str(i))
    webBrowser.get(homeUrl)
for i in range(len(mtzList)):
    webBrowser.switch_to.window(str(i))
    xpath_miui.uploadSingleMtz(webBrowser, wait, mtzList[i])
    time.sleep(3)
    webBrowser.close()
webBrowser.switch_to.window(mainWindow)
webBrowser.close()
