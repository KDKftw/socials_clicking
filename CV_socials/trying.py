import cv2
import numpy as np
import time
import pyautogui as p
#viewLocator = max_loc

##template to find to_name == the picture im looking for in the screenshot of the display, gotta be pre-set
def takeSS_findTemplateInScreen_clickOnTemplate(screenShotOfDisplay_name, templateToFindTo_name):

    ##take screen on initial page, save, find view, get location, click
    myScreenshot = p.screenshot()
    myScreenshot.save(screenShotOfDisplay_name+".png")
    screenshot = cv2.imread(screenShotOfDisplay_name+".png", 0)
    template = cv2.imread(templateToFindTo_name+".png",  0)
    res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    viewLocator = min_loc

    print(viewLocator)
    #print(cv2.minMaxLoc(res))
    time.sleep(2)
    p.click(viewLocator)

time.sleep(5)
takeSS_findTemplateInScreen_clickOnTemplate("screenshot1", "view4")
