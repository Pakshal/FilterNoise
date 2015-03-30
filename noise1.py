import cv2
import numpy as np
from matplotlib import pyplot as plt

#Reading the image
img = cv2.imread(ADD image path)#Enter the image path.

#Apply Gaussian filter on the image
blur = cv2.GaussianBlur(img,(5,5),0)

#Apply Gaussian filter on the blurred image
blur1 = cv2.GaussianBlur(blur,(5,5),0)

#Subtract the two images to get DoG
DoG=blur-blur1

#Plotting Original image
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

#Plotting DoG
plt.subplot(122),plt.imshow(DoG),plt.title('DoG')
plt.xticks([]), plt.yticks([])

#Display
plt.show()
