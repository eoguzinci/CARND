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

`$$ x+y=z $$`