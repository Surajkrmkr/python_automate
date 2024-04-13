import xpath_miui
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import data
import time

maxTab = 5
sequenceList = []

mtzList = []

for (root, dirs, file) in os.walk(data.path):
    for f in file:
        if '.mtz' in f:
            mtzList.append(f)


count = len(mtzList) // maxTab
rem = len(mtzList) % maxTab
if(rem != 0):
    count += 1
for i in range(count):
    sequenceList.append(mtzList[i * maxTab:(i + 1) * maxTab])

print(sequenceList)


options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
options.add_experimental_option('excludeSwitches', ['enable-logging'])
webBrowser = webdriver.Chrome(options=options)
webBrowser.maximize_window()

homeUrl = "https://in.zhuti.designer.intl.xiaomi.com/"
# homeUrl = "https://zhuti.designer.intl.xiaomi.com/"

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

for i in range(len(sequenceList)):
    for j in range(len(sequenceList[i])):
        webBrowser.execute_script("window.open('about:blank',"+str(j)+");")
        webBrowser.switch_to.window(str(j))
        webBrowser.get(homeUrl)
    for j in range(len(sequenceList[i])):
        webBrowser.switch_to.window(str(j))
        xpath_miui.uploadSingleMtz(webBrowser, wait, sequenceList[i][j])
        time.sleep(3)
        webBrowser.close()
    webBrowser.switch_to.window(mainWindow)

webBrowser.switch_to.window(mainWindow)
webBrowser.close()
