import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image1_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigastand.jpg"
image2_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigasit.jpg"

image1 = cv.imread(image1_path, cv.IMREAD_GRAYSCALE)
image2 = cv.imread(image2_path, cv.IMREAD_GRAYSCALE)

if image1.shape != image2.shape:
    image2 = cv.resize(image2, (image1.shape[1], image1.shape[0]))

# intersection = np.zeros_like(image1)
# rows, cols = image1.shape

# for i in range(rows):
#     for j in range(cols):
#         if image1[i,j] == image2[i,j]:
#             intersection[i,j] = image1[i,j]

intersection = cv.bitwise_and(image2, image1)

#bitwise or
orr = cv.bitwise_or(image1, image2)

#bitwise xor
xor = cv.bitwise_xor(image1, image2)


plt.figure(figsize=(10,10))
plt.subplot(2,3,1)
plt.imshow(image1, cmap='gray')
plt.title("Image 1")
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(image2, cmap='gray')
plt.title("Image 2")
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(intersection, cmap='gray')
plt.title("Intersection")
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(orr, cmap='gray')
plt.title("OR")
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(xor, cmap='gray')
plt.title("XOR")
plt.axis('off')

plt.tight_layout()
plt.show()
