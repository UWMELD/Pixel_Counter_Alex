import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

img_orig = cv2.imread('draw1.png') #BGR
# img = cv2.imread('draw3.png') #BGR
img = cv2.resize(img_orig, (int(img_orig.shape[1]/2), int(img_orig.shape[0]/2)), interpolation = cv2.INTER_AREA)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey(0)

denom = 8
height, width, channels = img.shape
print(img_orig.shape)
print(img.shape)
full_area = height*width
block_size = int(math.sqrt(full_area/denom)/3)
# block_size = 130
drawn_area = 0

print('block-size: ',block_size)

def has_color(i, j):
    cnt = 0
    for r in range(block_size):
        for c in range(block_size):
            if block_size*i+r>=height or block_size*j+c>=width:
                continue
            elif int(img[block_size*i+r][block_size*j+c][0])+int(img[block_size*i+r][block_size*j+c][1])+int(img[block_size*i+r][block_size*j+c][2]) in range(255, 760):
                cnt+=1

                if cnt >= 0.1*block_size*block_size:
                    print('colored')
                    return True

def paint(i, j):
    global drawn_area
    for r in range(block_size):
        for c in range(block_size):
            if block_size*i+r>=height or block_size*j+c>=width:
                continue
            elif r==0 or r==block_size-1 or c==0 or c==block_size-1:
                img[block_size*i+r][block_size*j+c][0] = 240
            else:
                img[block_size*i+r][block_size*j+c][0] = 0
            img[block_size*i+r][block_size*j+c][1] = 0
            img[block_size*i+r][block_size*j+c][2] = 240
    drawn_area+=1

for i in range(int(height/block_size)+1):
    for j in range(int(width/block_size)+1):
        print(i,j)
        if has_color(i,j):
            paint(i,j)

# count red
pix_cnt = 0
for i in img:
    for j in i:
        if(j[0]==0 and j[1]==0 and j[2]==240):
            pix_cnt+=1
        
    
cv2.imshow('image',img)
cv2.waitKey(0)

print('full: ', full_area)
print('drawn: ', pix_cnt)
print('ratio: ', pix_cnt/full_area)