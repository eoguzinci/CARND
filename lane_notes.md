<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$']],
      displayMath: [ ['$$','$$']],
      processEscapes: true
    },
    "HTML-CSS": { availableFonts: ["TeX"] }
  });
</script>
# COMPUTER VISION
Until now, we have learned to mask some part of the image and put a threshold to rgb values to cancel the colors intended.

If we do them both (color_threshold and masking), you can change the color of patterns with specific colors (colors with high RGB -> some other colors defined). 

But these are not enough because the color of the shapes or patterns varies through the video. Therefore,  we need to utilize more complex algorithms for pattern detection.

## Canny Edge Detection
image -> grayscale -> gradient of grayscale

The gradient detects the boundaries of the given shapes from background or other patterns. As we think the image as a 2D domain in x and y, we must take derivative in both directions. The gradient gives us thick edges, however we need thin edges to clearly detect the boundaries. Therefore, we use Canny algorithm.

**Note:** The origin of the image is at top left. Therefore, x increases when you go right of image (*that's ok actually*),but y increases when you go down. But you must think the image as a matrix. That will enhance your understanding about the images and their coordinates (`image[0][0] -> top_left`).

### __In code__:

Import plotting module of matplotlib : `import matplotlib.pyplot as plt`

Import image module of matplotlib : `import matplotlib.image as mpimg`

The first thing to do is importing image via matplotlib with `mpimg.imread(<figure_file>)`.

If you want to visualize this figure later, please assign it to variable such as: `image = mpimg.imread('exit-ramp.jpg')`

Then you can plot it with `plt.imshow(image)`

Then Canny edge detector needs 2 parameters: 
1. high threshold
2. low threshold

The pixels with lower RGB values than the low threshold will be rejected. The pixels with higher RGB

## HOMEWORK Notes - Lane Detection from the image

### __Reference Solution__: 

#### Canny edge detection: 
low_threshold : 50
high_threshold : 150

#### Region selection : 
`vertices = np.array([[(0,imshape[0]),(450, 290), (490, 290), (imshape[1],imshape[0])]], dtype=np.int32)`

#### Parameters for Hough space: 
##### Grid parameters
    `rho = 2` (pixels)
    `theta = np.pi/180` (in radians = 1 degree)
    `threshold = 15`  (meaning at least 15 points in image space need to be associated with each line segment)
    `min_line_length = 40` (pixels)
    `max_line_gap = 20` (pixels).

With these parameters, I'm picking up the lanes lines and nothing else, so looks like a decent solution!

