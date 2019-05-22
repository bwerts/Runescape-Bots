import pyautogui as pag
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt

def clicknav(clicky):
#converts testfind-template image to grayscale then locates and outlines
#mining locations with the tin-template image.
    img_rgb = cv2.imread('testfind-template.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('tin-template.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    #
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draws red square box around matched images
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,155), 1)
    #writes new image called finds.png from the img_gray(testfind-template) image
    cv2.imwrite('finds.png',img_rgb)

clicknav(0)
