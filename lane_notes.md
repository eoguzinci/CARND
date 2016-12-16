# COMPUTER VISION
Until now, we have learned to mask some part of the image and put a threshold to rgb values to cancel the colors intended.

If we do them both (color_threshold and masking), you can change the color of patterns with specific colors (colors with high RGB -> some other colors defined). 

But these are not enough because the color of the shapes or patterns varies through the video. Therefore,  we need to utilize more complex algorithms for pattern detection.

## Canny Edge Detection
image - > grayscale -> gradient of grayscale

The gradient detects the boundaries of the given shapes from background or other patterns. As we think the image as a 2D domain in x and y, we must take derivative in both directions. The gradient gives us thick edges, however we need thin edges to clearly detect the boundaries. Therefore, we use Canny algorithm.

