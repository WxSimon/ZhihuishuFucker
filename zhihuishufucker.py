from selenium import webdriver
from time import *

global tryTimer
global chromedriver
global currentElement

def tryPress():
    print('tryPress')
    try:
        popBtnCancel = chromedriver.find_element_by_class_name("popbtn_cancel")
        popBtnCancel.click()
    except:
        print("no element cancel")

    try:
        popBtnYes = chromedriver.find_element_by_class_name("popbtn_yes")
        popBtnYes.click()
    except:
        print("no element yes")

def checkVideo():
    print("checkVideo")

    playButton = chromedriver.find_element_by_id("playButton")
    playStutusClass = playButton.get_attribute("class")
    if playStutusClass == "playButton":
        return True

    else:
        return False

def zhangVideo(zhang, jie, xiaojie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d.%d']"% (zhang,jie,xiaojie))
        nextbtn.click()
    except:
        print("no element cancel")

def nextZhangVideo(zhang, jie, xiaojie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d']" % (zhang, jie))
        nextbtn.click()
    except:
        zhangVideo(zhang, 1, 1)

def jieVideo(zhang, jie, xiaojie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d.%d']" % (zhang,jie,xiaojie))
        nextbtn.click()
    except:
        nextZhangVideo(zhang + 1, 1, 1)

def nextJieVideo(zhang, jie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d']" % (zhang,jie))
        nextbtn.click()
    except:
        jieVideo(zhang, jie, 1)

def nextVideo(zhang, jie, xiaojie):
    print("nextVideo")

    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d.%d']"% (zhang,jie,xiaojie))
        nextbtn.click()
    except:
        nextJieVideo(zhang, jie+1)


if __name__ == "__main__":

    driverpath = "__driverpath__/chromedriver"
    chromeOption = webdriver.ChromeOptions()

    chromedriver = webdriver.Chrome(executable_path=driverpath, chrome_options=chromeOption)

    chromedriver.get("http://online.zhihuishu.com/CreateCourse/learning/videoList?courseId=2005094&rid=4332")
    chromedriver.maximize_window()

    usernameInput = chromedriver.find_element_by_id("lUsername")
    pswInput = chromedriver.find_element_by_id("lPassword")

    usernameInput.send_keys("username")
    pswInput.send_keys("password")

    chromedriver.find_element_by_class_name("wall-sub-btn").click()

    sleep(5)
    tryPress()

    while True:
        sleep(10)
        tryPress()
        if checkVideo():
            print("next")

            currentElement = chromedriver.find_element_by_class_name("current_play")

            zhangnum = int(currentElement.get_attribute("_zhangnum"))
            jienum = int(currentElement.get_attribute("_jienum"))

            try:
                currentXiaojie = currentElement.get_attribute("_xjienum")
                xiaojienum = int(currentXiaojie)
            except:
                xiaojienum = 0
                jienum += 1

            nextVideo(zhangnum, jienum, xiaojienum+1)

    chromedriver.quit()
