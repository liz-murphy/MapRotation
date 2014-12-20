#!/usr/bin/python
'''
This example illustrates how to use Hough Transform to find lines
Usage: ./houghlines.py [<image_name>]
image argument defaults to ../data/pic1.png
'''
import cv2
import numpy as np
import sys
import math
import scipy
from scipy.misc import imrotate
from PIL import Image
from scipy import ndimage

try:
        fn = sys.argv[1]
except:
        fn = "map.png"
        print __doc__
        src = cv2.imread(fn)
        dst = cv2.Canny(src, 50, 200)
        cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

print 'Press any key to continue, space to accept 0 degree line'

lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 50, np.array([]), 50, 10)
a,b,c = lines.shape
for i in range(b):
        cv2.line(cdst, (lines[0][i][0], lines[0][i][1]), (lines[0][i][2], lines[0][i][3]), (0, 0, 255), 3, cv2.CV_AA)

        cv2.imshow("source", src)
        cv2.imshow("detected lines", cdst)
        a = cv2.waitKey(0)
        if a == 1048608:
            print 'Aligning to this line'
            break

angle = math.atan2( (lines[0][i][3]-lines[0][i][1]),(lines[0][i][2]-lines[0][i][0]) )
print "Angle of rotation: " + str(angle)

rotated = ndimage.rotate(src, 180*angle/3.1415, (1,0), True, None, 0, 'constant', 205, True)
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)
cv2.imwrite('aligned.png', rotated, [cv2.cv.CV_IMWRITE_PNG_COMPRESSION,9])
#cv2.imwrite('aligned.pgm', rotated)

