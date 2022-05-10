from scipy import ndimage
import cv2 as cv
import numpy as np
import FindingShapesNoise as fs
import RunShapesOnIMG as RS

#Changes the image angle

def SwichAngle(GetImage):
 print('Enter the angle size:')
 Xangle=input()
 print('')
 xa=np.int(Xangle)
 rotated = ndimage.rotate(GetImage, xa)

 # Reduces black background
 height, width, _ = rotated.shape
 if GetImage[0,0].sum() != 0 and xa!=90 and xa!=180 and xa!=270 and xa!= 360:
  for i in range(height):
   for j in range(width):
    if rotated[i, j].sum() == 0:
     rotated[i, j] = GetImage[0, 0]
 return rotated

#Running the algorithm
def ShowAngle(Getimg):
 AngleIMG = SwichAngle(Getimg.copy())
 NewIMG=unsharp_mask(AngleIMG.copy())
 RS.ColoringShapes(NewIMG.copy())


#After changing the image angle, we can lose pixels
#This function helps us to reduce pixel loss and sharpens the image
def unsharp_mask(image, kernel_size=(7, 7), sigma=1.0, amount=2.0, threshold=0):

    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened