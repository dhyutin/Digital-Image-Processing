import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("PISA.jpg",0)
cv2.imshow('Original',img)
cv2.waitKey(0)
print(img.shape)
a=(18*math.pi/180)
hgt=img.shape[0]
wdt=img.shape[1]
print(img.shape)
new=np.zeros([224,225],dtype=np.uint8)
rotated=np.zeros([224,225],dtype=np.uint8)
# cv2.imshow('original',img)
# cv2.waitKey(0)
for i in range(224):
    for j in range(225):
        x_cord=int(i*math.cos(a)-j*math.sin(a))
        y_cord=int((i*math.sin(a)+j*math.cos(a)))
        if(x_cord<224 and y_cord<225):
            new[x_cord][y_cord] = img[i][j];
            rotated[x_cord][y_cord] = img[i][j];
cv2.imshow('rotated',new) #rotated image without bilinear interpolation
cv2.waitKey(0)
# cv2.destroyAllWindows()
for i in range(224):
    for j in range(225):
        if( new[i][j]==0):
            print(i,j)
            if(i>0 and j>0 and i<223 and j<223):
                new[i][j]=0.25*(rotated[i-2][j-2]+rotated[i-2][j]+rotated[i][j]+rotated[i][j-1])

cv2.imshow('new_rot',new)
cv2.waitKey(0)
cv2.destroyAllWindows()