import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\hansleep.jpg"

image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

rmax = np.max(image)
rmin = np.min(image)
L = 255

stretched = (((image - rmin) / (rmax - rmin)) * 255).astype(np.uint8)

plt.subplot(2,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(stretched, cmap='gray')
plt.title('Stretched Image')
plt.axis('off')

plt.subplot(2,2,3)
plt.hist(image.ravel(), bins=256, color='gray')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(2,2,4)
plt.hist(stretched.ravel(), bins=256, color='gray')
plt.title('Stretched Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()  

