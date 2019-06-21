# coding=utf-8
import moment
import allure
import json
import inspect
import os

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "admin"
PASSWORD = "admin123"

def whoami():
    return inspect.stack()[1][3]

def screenshot(self,casename):
    print("inside ScreenShot Def")
    timeFormat = moment.now().strftime("%d-%m-%y_%H-%M-%S")
    picName =casename+"_"+timeFormat
    print("Captured the Screenshot named :",picName)
    allure.attach(self.driver.get_screenshot_as_png(),name=picName,attachment_type=allure.attachment_type.PNG)

def cleanfolder(path):
    if os.path.exists(path):
        for i in os.listdir(path):
            file_path = os.path.join(path,i)
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                cleanfolder(file_path)