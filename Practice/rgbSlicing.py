import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigasit.jpg"

image = cv.imread(image_path)



b, g, r = cv.split(image)


plt.subplot(2,3,1)
plt.imshow(r, cmap='Reds')
plt.axis("off")
plt.title("Red channel")

plt.subplot(2,3,2)
plt.imshow(g, cmap='Greens')
plt.axis("off")
plt.title("Green Channel")

plt.subplot(2,3,3)
plt.imshow(b, cmap='Blues')
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2,3,4)
plt.hist(r.ravel(), bins=256, color='red')
plt.xlim([0,255])

plt.subplot(2,3,5)
plt.hist(g.ravel(), bins=256, color='green')
plt.xlim([0,255])

plt.subplot(2,3,6)
plt.hist(b.ravel(), bins=256, color='blue')
plt.xlim([0,255])

plt.tight_layout()
plt.show()