# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 03:55:06 2017

@author: mayank
"""

import numpy
import cv2

cap=cv2.VideoCapture('E:/video.avi')
print("VideoPlayer")
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.resizeWindow('Videoplayer',640,340)
    cv2.imshow('VideoPlayer',frame)
    if cv2.waitKey(25)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()