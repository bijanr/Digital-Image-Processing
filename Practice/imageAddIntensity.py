import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigasit3.jpg"

image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
#or cv.imread(image_path, cv.COLOR_BGR2GRAY)


resize = cv.resize(image, (256,256))

modified = cv.add(resize, -100)
#cv.convertScaleAbs(resize, alpha=1, beta=20)

plt.subplot(2,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(resize, cmap='gray')
plt.title('Resized Image')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(modified, cmap='gray')
plt.title('Modified Image (by -100)')
plt.axis('off')

plt.tight_layout()
plt.show()  