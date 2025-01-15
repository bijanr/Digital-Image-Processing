import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\hansleep.jpg"

image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

image1D = image.ravel()
histogram, bins  = np.histogram(image1D, bins=256, range=[0, 256])

total_pixels = image.size
pdf = histogram / total_pixels

# Cumulative Distribution Function (CDF)
cdf = pdf.cumsum()

# Minimum non-zero CDF value
normalized_cdf = (cdf * 255).astype(np.uint8)


# mapping original image with modified cdf
enhancd_image = normalized_cdf[image1D].reshape(image.shape)

plt.subplot(2,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(enhancd_image, cmap='gray')
plt.title('Enhanced Image')
plt.axis('off')

plt.subplot(2,2,3)
plt.hist(image.ravel(), bins=256, color='gray')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(2,2,4)
plt.hist(enhancd_image.ravel(), bins=256, color='gray')
plt.title('Enhanced Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

