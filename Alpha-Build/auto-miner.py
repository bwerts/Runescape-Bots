import pyautogui as pag
import time
import cv2
import numpy as np
import random

def screen_adjust(rd, rp):
#adjusts the screen so everything will align
    time.sleep(2)
    wrench = pag.locateCenterOnScreen("wrench.png")
    pag.moveTo(wrench, duration=rd, pause=rp)
    pag.click()
    pag.moveTo(1810, 735, duration=rd, pause=rp)
    pag.click()
    pag.moveTo(1720, 56, duration=rd, pause=rp)
    pag.click()

    pag.keyDown('up')
    time.sleep(1)
    pag.keyUp('up')

def tin1():
#takes screenshot in general location of left node and uses image recognition
#to decide if the node it minable.
    time.sleep(1)
    pag.screenshot('tin1-shot.png', region=(863,545, 178,142))
    screen = cv2.imread('tin1-shot.png')
    template = cv2.imread('tin-template.png')

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = .80
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        return True
    else:
        return False
    #    cv2.imwrite('res.png',screen)
def tin2():
#takes screenshot in general location of right node and uses image recognition
#to decide if the node it minable.
    time.sleep(1)
    pag.screenshot('tin2-shot.png', region=(962,561, 179,143))
    screen2 = cv2.imread('tin2-shot.png')
    template2 = cv2.imread('tin-template.png')

    res = cv2.matchTemplate(screen2, template2, cv2.TM_CCOEFF_NORMED)
    threshold = .80
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        return True
    else:
        return False
    #    cv2.imwrite('res.png',screen)
def random_cord(rlx, rly, click_point):
#takes random location if both mining nodes are up (true) and generates
#random locations inside one of the square mining nodes to click on.
    x1, y1 = (rlx, rly)
    x2, y2 = (click_points[0], click_points[1])
    x2 = random.randint(1, x2+2)
    y2 = random.randint(1, y2)

    cords = (int(x1)+int(x2), int(y1)+int(y2))
    pag.moveTo(cords[0], cords[1], duration=rd, pause=rp)
    pag.click()

#top left x and y cordinates for mining locations
locations = ['937-,586', '1020,577']
#picks a random location from the locations list
rand = (random.choice(locations))
#removes the - used as placeholder for 3 digit X values
rlx = (rand[:4].replace('-',''))
rly = rand[5:]
#generates random #'s that are less than 1
#for mouse duration an pause
rd = random.uniform(0.23, 0.40)
rp = random.uniform(0.20, 0.30)
click_points = [60, 50]
start_points = [rlx, rly]

screen_adjust(rd, rp)
#nodes on tutorial island respawn too quick, can't test true/false outcomes
#only True/True
if tin1() and tin2() is True:
    random_cord(rlx, rly, click_points)
else:
    print ("one is false")
