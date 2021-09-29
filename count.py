import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('draw.png') #BGR
cv2.imshow('image',img)
cv2.waitKey(0)

full_area = img.shape[0]*img.shape[1]
drawn_area = 0

for i in img:
    
    for j in i:
        if(j[0]!=0 and j[0]!=255 and j[1]!=0 and j[1]!=255 and j[1]!=0 and j[1]!=255):
            j[0] = 0
            j[1] = 0
            j[2] = 255
            drawn_area+=1
        else:
            j[0] = 0
            j[1] = 0
            j[2] = 0
cv2.imshow('image',img)
cv2.waitKey(0)

print('full: ', full_area)
print('drawn: ', drawn_area)
print('ratio: ', drawn_area/full_area)