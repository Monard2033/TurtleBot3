#!/usr/local/bin/python3

import cv2
import numpy as np

def draw_line(p1, p2):
    for p in np.linspace(p1, p2, np.linalg.norm(p1-p2)):
        image[tuple(np.int32(p))] = [0,0,255]

def check_line(p1, p2):
    for p in np.linspace(p1, p2, np.linalg.norm(p1-p2)):
        pos = tuple(np.int32(p))
        if not (imageo[pos[0],pos[1],0] == 254 and imageo[pos[0],pos[1],1] == 254 and imageo[pos[0],pos[1],2] == 254):
            return False
    return True


image = cv2.imread('world.pgm')
imageo = cv2.imread('world.pgm')
height, width, channels = image.shape

red = [0,0,255]
white = [254,254,254]

pt_a = np.array([0, 0])
pt_b = np.array([225, 195])

#draw_line(pt_a, pt_b)
def calculate_point():
 for x in range(0,width):
    for y in range(0,height):
        crt = np.array([x, y])
        if check_line(crt, pt_b):
            image[x,y] = [0,0,255]
            
cv2.imwrite("result.png",image)

