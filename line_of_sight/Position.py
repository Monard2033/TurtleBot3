#!/usr/local/bin/python3

import cv2
import numpy as np
from decimal import *

image = cv2.imread('world.pgm')
imageo = cv2.imread('result.png')

def draw_line(p1, p2):
    for p in np.linspace(p1,p2, np.linalg.norm(p1-p2)):
        image[tuple(np.int32(p))] = [0,0,255]
        
def check_point(p1):
    if (imageo[p1[0],p1[1],0] == 254 and imageo[p1[0],p1[1],1] == 254 and imageo[p1[0],p1[1],2] == 254):
          print(p1)
          cv2.imwrite("result3.png",imageo)
          return True
    return False

height, width, channels = image.shape

red = [0,0,255]
white = [254,254,254]

pt_a = np.array([0, 0])
pt_b = np.array([222, 195])


def calculate_goal():
    height, width, channels = image.shape
    for x in range(0,width):
     for y in range(0,height):
        crt = np.array([x, y])
        print(crt)
        varx = Decimal(225//(0.85+4.1)//20)
        vary = Decimal(195//(0.85+3.8)//20)
        print(varx,vary)
        crt0=Decimal(x)//Decimal(varx) #(76.43)
        crt1=Decimal(y)//Decimal(vary) #(83.7)
        if(crt0>= Decimal(1.13)):
          crt1=Decimal(y)/Decimal(102.4)
        if(crt0>=Decimal(225)/Decimal(78.6)):
            crt0= -abs(crt0)
        crt2 = round(crt0, 5)
        crt3 = round(crt1, 5)
        if check_point(crt):
         return np.array([crt2,crt3])


