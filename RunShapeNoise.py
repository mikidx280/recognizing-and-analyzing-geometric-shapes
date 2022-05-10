import numpy as np
import cv2
from matplotlib import pyplot as plt
import FindingShapesNoise as Sid
import Noise as ns
import ChangeAngle as ca
import cv2.ximgproc as gd


def ShapeOnNiose(getIMG):

 ImageORG1=getIMG

 # Runs the shape recognition with noise

 x=1

 while x != -1:
    print('Please enter the number of the noise type:')
    print('1:gauss  2:s&p')
    print('To end the Noise mod program, press -1')
    TypeOfNoise=input()
    print('')
    print('')
    x=np.int(TypeOfNoise)
    if x==1:
        nioseIMG = ns.noisy("gauss", ImageORG1.copy())
        grayScale = cv2.cvtColor(nioseIMG, cv2.COLOR_BGR2GRAY)
        #Filter that reduce noise
        dst4 = cv2.fastNlMeansDenoising(grayScale,None,60,10,21)
        dst5 = cv2.cvtColor(dst4, cv2.COLOR_GRAY2BGR)
        title='Noise gauss'
        NewNioseImg = Sid.ShapeID(nioseIMG.copy(),dst5.copy())
        plt.subplot(121)
        plt.title(title)
        plt.imshow(cv2.cvtColor(nioseIMG, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])
        plt.subplot(122)
        plt.title('Coloring the shapes')
        plt.imshow(cv2.cvtColor(NewNioseImg, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])
        plt.show()

    elif x==2:

        nioseIMG = ns.noisy("s&p", ImageORG1.copy())
        grayScale = cv2.cvtColor(nioseIMG, cv2.COLOR_BGR2GRAY)
        # Filter that reduce noise
        dst4 = cv2.fastNlMeansDenoising(grayScale, None, 60, 10, 21)
        dst5 = cv2.cvtColor(dst4, cv2.COLOR_GRAY2BGR)
        NewNioseImg = Sid.ShapeID(nioseIMG.copy(), dst5.copy())
        title = 'Noise s&p'
        plt.subplot(121)
        plt.title(title)
        plt.imshow(cv2.cvtColor(nioseIMG, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])
        plt.subplot(122)
        plt.title('Coloring the shapes')
        plt.imshow(cv2.cvtColor(NewNioseImg, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])
        plt.show()


    elif x == -1:
        print('end  of the Noise mod program')
        print('')

    else:
        print('The user has not entered any of the options')
        print('')










