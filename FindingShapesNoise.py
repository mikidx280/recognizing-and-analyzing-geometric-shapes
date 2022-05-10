from __future__ import print_function
import numpy as np
import cv2



def ShapeID (ImageFromUser,GrayIMG):
    image=ImageFromUser


    # convert the filtered gray image into grayscale
    grayScale = cv2.cvtColor(GrayIMG, cv2.COLOR_BGR2GRAY)

    # Find edges in the image using canny edge detection method
    # Calculate lower threshold and upper threshold using sigma = 0.33
    sigma = 0.33
    v = np.median(grayScale)
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))



    edged = cv2.Canny(grayScale, lower_thresh, upper_thresh)



    # After finding edges we have to find contours

    cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.RETR_EXTERNAL is passed to find the outermost contours (because we want to outline the shapes)
    # cv2.CHAIN_APPROX_SIMPLE is removing redundant points along a line





    # Now we will loop over every contour
    # call detectShape() for it and
    # write the name of shape in the center of image

    # loop over the contours
    for c in cnts:

        shape='unknown'

        # calculate perimeter using
        peri = cv2.arcLength(c, True)

        # apply contour approximation and store the result in vertices
        epsilon = 0.03 * peri

        vertices = cv2.approxPolyDP(c, epsilon, True)

        # If the shape is triangle, it will have 3 vertices
        if len(vertices) == 3:
        #It will color it green
            cv2.drawContours(image, [c], 0, (0, 255, 0), 5)

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        elif len(vertices) == 4:
            # using the boundingRect method calculate the width and height
            # of enclosing rectange and then calculte aspect ratio

            x, y, width, height = cv2.boundingRect(vertices)
            aspectRatio = float(width) / height

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                shape = "square"
                # It will color it pink
                cv2.drawContours(image, [c], 0, (180, 105, 255), 5)
            else:
                shape = "rectangle"
                # It will color it Dark Blue
                cv2.drawContours(image, [c], 0, (255, 0, 0), 5)

        # if the shape is a pentagon, it will have 5 vertices
        elif len(vertices) == 5:
            # It will color it dark pink
            cv2.drawContours(image, [c], 0, (204, 0, 102), 5)
        # if the shape is a hexagon, it will have 6 vertices
        elif len(vertices) == 6:
            # It will color it Gold
            cv2.drawContours(image, [c], 0, (0, 128, 128), 5)
        # if the shape is a star, it will have 10 vertices
        elif len(vertices) == 10:
            # It will color it Yellow
            shape = "star"
            cv2.drawContours(image, [c], 0, (0, 255, 255), 5)
        else:
            shape = "circle"
            # It will color it Red
            cv2.drawContours(image, [c], 0, (0, 0, 255), 5)







 # show the output image
    return image




