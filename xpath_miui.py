
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import data

signIn = "//*[@id=\"app\"]/div/div[2]/div/button[1]"
signInUsingPw = "//*[@id='rc-tabs-0-panel-login']/form/div[1]/div[3]/div/a"
emailId = "//input[@name='account']"
pw = "password"
submit = "//button[@type='submit']"
submitBtn = "//*[@id=\"app\"]/section/div[2]/div[1]/div[1]/div/div[2]/button"
cookieBtn = "//*[@id=\"__cookie_tip\"]/div"
dialogOkBtn = '//*[@id="app"]/section/div[2]/div[2]/div/div[3]/div/button'
fileDrag = "//*[@class=\"upload-area\"][3]//input"
desc = "//textarea[contains(@placeholder,'Describe this theme')]"
tags = "//input[contains(@placeholder,'tags')]"
tagError = "//div[contains(text(),'no such')]"
copyrightFile = "//input[contains(@accept,'.zip')]"
finalBtn = "//span[contains(@slot,'footer')]/button"


def uploadSingleMtz(webBrowser, wait, file: str):
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, submitBtn)))
    webBrowser.execute_script(
        "arguments[0].click();", webBrowser.find_element(By.XPATH, submitBtn))
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, fileDrag)))
    webBrowser.find_element(By.XPATH, fileDrag).send_keys(
        data.path+"\\"+file)
    wait.until(EC.presence_of_element_located((By.XPATH, desc)))
    webBrowser.find_element(By.XPATH, desc).send_keys(
        "Features:\r\n" + "- Digital Clock\r\n" + "- Icons\r\n" + "- Music\r\n" + "- WeekDay")
    webBrowser.execute_script("scroll(350, 0)")
    webBrowser.find_element(By.XPATH, copyrightFile).send_keys(
        data.path+"\\1copyright\\"+file.replace(".mtz", ".zip"))
    time.sleep(5)
    while(True):
        webBrowser.find_element(By.XPATH, tags).clear()
        with open(data.path+"\\1tags\\"+file.replace(".mtz", ".txt")) as f:
            line = f.read().split(",")
        for tag in line:
            webBrowser.find_element(By.XPATH, tags).send_keys(tag)
            time.sleep(2)
            webBrowser.find_element(By.XPATH, tags).send_keys(Keys.ENTER)
        try:
            webBrowser.find_element(By.XPATH, tagError)
        except:
            break

    webBrowser.find_element(By.XPATH, finalBtn).click()
    print(file)
