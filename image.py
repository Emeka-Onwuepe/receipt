
import cv2 as cv 
import numpy as np

image = cv.imread('./logo.png')

image_copy = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#_,image_copy = cv.threshold(image_copy,191,255,cv.THRESH_BINARY)

cv.imwrite('logo2.png',image_copy)

