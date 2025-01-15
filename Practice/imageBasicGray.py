import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#for input grayscale image from default rgb image
image = cv.imread(r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\hansleep.jpg", cv.IMREAD_GRAYSCALE)

#for moodified grayscale image
grayimage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
#cv reads image in BGR format, so we need to convert it to RGB format for matplotlib
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGBA))
plt.axis("off")
plt.title("original image")

#plotting the grayscale image
plt.subplot(1, 2, 2)
plt.imshow(grayimage, cmap="gray")
plt.axis("off")
plt.title("HLS image")
plt.tight_layout()
plt.show()
