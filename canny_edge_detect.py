# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 01:30:53 2016

@author: oguzi
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('exit-ramp.jpg')
fig1 = plt.figure()
plt.imshow(image)

import numpy as np
import cv2  #bringing in OpenCV libraries
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
fig2 = plt.figure()
plt.imshow(gray, cmap='gray')
 
# Define a kernel size for Gaussian smoothing / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

# Define parameters for Canny and run it
# NOTE: if you try running this code you might want to change these!
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(gray, low_threshold, high_threshold)

# Display the image
fig3 = plt.figure()
plt.imshow(edges, cmap='Greys_r')
plt.savefig('exit-ramp_det.png')