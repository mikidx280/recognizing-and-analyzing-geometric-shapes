import numpy as np
import cv2
from matplotlib import pyplot as plt
import RunShapeNoise as RSn
import RunShapesOnIMG as RS
import ChangeAngle as CA
import Noise as ns

#Reads the pictures
img1=cv2.imread('ImgGeo.jpg')
img2=cv2.imread('geoshapes1.png')
# Runs geometric shape recognition and colors them according to the following categories
# 1:Triangle-Green 2: Square-Pink 3: Rectangle-Blue 4: Star-Yellow 5: Circle-Red
RS.ColoringShapes(img1.copy())
RS.ColoringShapes(img2.copy())
# Runs geometric shape recognition on noise and colors them according to the following categories
# 1:Triangle-Green 2: Square-Pink 3: Rectangle-Blue 4: Star-Yellow 5: Circle-Red
RSn.ShapeOnNiose(img1.copy())
print('for Image number 1')
print('')
print('The noise mod has been continued for Image number 2')
print('')
RSn.ShapeOnNiose(img2.copy())
# Changes the angle of the IMG and colors them according to the following categories
# 1:Triangle-Green 2: Square-Pink 3: Rectangle-Blue 4: Star-Yellow 5: Circle-Red

flag=1
while flag !=-1:
 CA.ShowAngle(img2)
 print('If you want to stop switch mod angle please press -1')
 print('Else press other number')
 print('')
 flag_x = input()
 flag = np.int(flag_x)

