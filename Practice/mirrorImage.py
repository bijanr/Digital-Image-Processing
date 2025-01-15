import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\math1.jpg"

image = cv.imread(image_path, cv.COLOR_BGR2RGB)

hMirror = cv.flip(image, 0)
vMirror = cv.flip(image, 1)


plt.figure(figsize=(10,10))
plt.subplot(2,3,1)
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(cv.cvtColor(hMirror, cv.COLOR_BGR2RGB))
plt.title("Horizontal Mirror")
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(cv.cvtColor(vMirror, cv.COLOR_BGR2RGB))
plt.title("Vertical Mirror")
plt.axis('off')

#original image histogram
plt.subplot(2,3,4)
plt.hist(image.ravel(), 256, [0, 256])
plt.title("Original Image Histogram")
plt.ylabel("Frequency")
plt.xlabel("Pixel Value")

#horizontal mirror histogram
plt.subplot(2,3,5)
plt.hist(hMirror.ravel(), 256, [0, 256])
plt.title("Horizontal Mirror Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

#vertical mirror histogram
plt.subplot(2,3,6)
plt.hist(vMirror.ravel(), 256, [0, 256])
plt.title("Vertical Mirror Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


