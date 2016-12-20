# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 03:44:06 2016

@author: oguzi
"""

# Do relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from numpy import linalg as LA

# Read in and grayscale the image
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

fig3 = plt.figure()
plt.imshow(edges, cmap='Greys_r')

ysize = edges.shape[0]
xsize = edges.shape[1]
region_select = np.copy(edges)

# Define a triangle region of interest 
# Keep in mind the origin (x=0, y=0) is in the upper left in image processing
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz 
margin = 80.0
left_bottom = [0, ysize]
right_bottom = [xsize, ysize]
right_top = [xsize/2+margin,320]
left_top = [xsize/2-margin,320]

# Fit lines (y=Ax+B) to identify the  3 sided region of interest
# np.polyfit() returns the coefficients [A, B] of the fit
fit_top = np.polyfit((left_top[0], right_top[0]), (left_top[1], right_top[1]), 1)
fit_left = np.polyfit((left_bottom[0], left_top[0]), (left_bottom[1], left_top[1]), 1)
fit_right = np.polyfit((right_bottom[0], right_top[0]), (right_bottom[1], right_top[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > (XX*fit_top[0] + fit_top[1])) & \
                    (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))

# Color pixels red which are inside the region of interest
region_select[~region_thresholds] = [0]

fig4 = plt.figure()
plt.imshow(region_select)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 1 # distance resolution of Hough Space
theta = 1*np.pi/180 # angular resolution of Hough Space
threshold = 20 # minimum number of intersections in a grid cell in Hough Space
min_line_length = 60 # min length of a line
max_line_gap = 10 # max distance between segments(in pixels) that forms a single line

# Run Hough on edge detected image
lines = cv2.HoughLinesP(region_select, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)
# length_lines = LA.norm(lines[0][0][2]-lines[0][0][0],lines[0][0][3]-lines[0][0][1])

# Iterate over the output "lines" and draw lines on the blank
line_image = np.copy(image)*0 # creating a blank image in the same size with initial image to draw lines on
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

fig1 = plt.figure()
plt.imshow(line_image)
        
# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))

# Draw the lines on the edge image
fig2 = plt.figure()
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(combo)
plt.savefig('exit-ramp_lane_detect.png')
