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
        return False

def nextZhangVideo(zhang, jie, xiaojie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d']" % (zhang, jie))
        nextbtn.click()
    except:
        return zhangVideo(zhang, 1, 1)

def jieVideo(zhang, jie, xiaojie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d.%d']" % (zhang,jie,xiaojie))
        nextbtn.click()
    except:
        return nextZhangVideo(zhang + 1, 1, 1)

def nextJieVideo(zhang, jie):
    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d']" % (zhang,jie))
        nextbtn.click()
    except:
        return jieVideo(zhang, jie, 1)

def nextVideo(zhang, jie, xiaojie):
    print("nextVideo")

    try:
        nextbtn = chromedriver.find_element_by_css_selector("li[_order='%d.%d.%d']"% (zhang,jie,xiaojie))
        nextbtn.click()
    except:
        return nextJieVideo(zhang, jie+1)


if __name__ == "__main__":

    driverpath = "/Users/sunkai07/Plugins/chromedriver"
    chromeOption = webdriver.ChromeOptions()
    prefs = {"download.default_dictionary": "/users/sunkai/desktop"}
    chromeOption.add_experimental_option("prefs", prefs)

    chromedriver = webdriver.Chrome(executable_path=driverpath, chrome_options=chromeOption)

    chromedriver.get("http://online.zhihuishu.com/CreateCourse/learning/videoList?courseId=2005094&rid=4332")
    chromedriver.maximize_window()

    usernameInput = chromedriver.find_element_by_id("lUsername")
    pswInput = chromedriver.find_element_by_id("lPassword")

    usernameInput.send_keys("17600200421")
    pswInput.send_keys("sskk999555")

    chromedriver.find_element_by_class_name("wall-sub-btn").click()

    sleep(5)
    tryPress()

    while True:
        sleep(10)
        tryPress()
        if checkVideo():
            print("切换视频")

            currentElement = chromedriver.find_element_by_class_name("current_play")

            zhangnum = int(currentElement.get_attribute("_zhangnum"))
            jienum = int(currentElement.get_attribute("_jienum"))

            try:
                currentXiaojie = currentElement.get_attribute("_xjienum")
                xiaojienum = int(currentXiaojie)
            except:
                xiaojienum = 0
                jienum += 1

            if not nextVideo(zhangnum, jienum, xiaojienum+1):
                if not nextVideo(zhangnum, jienum+1, 1):
                    nextVideo(zhangnum+1, 1, 1)

    chromedriver.quit()