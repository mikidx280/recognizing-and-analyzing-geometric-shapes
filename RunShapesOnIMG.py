import numpy as np
import cv2
from matplotlib import pyplot as plt
import FindingShapes as Sid
import Noise as ns

def ColoringShapes(GetImg):

    #Runs the shape recognition without noise
    print('The images after identifying the shapes')
    print('')
    print('')
    NewIMG=Sid.ShapeID(GetImg.copy())
    title = 'Original image'
    plt.subplot(121)
    plt.title(title)
    plt.imshow(cv2.cvtColor(GetImg.copy(), cv2.COLOR_BGR2RGB))
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.title('Coloring image with the shapes')
    plt.imshow(cv2.cvtColor(NewIMG.copy(), cv2.COLOR_BGR2RGB))
    plt.xticks([])
    plt.yticks([])
    plt.show()