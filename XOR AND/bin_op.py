import cv2
import numpy as np
import matplotlib.pyplot as plt

image1_path = r'C:\Bijan\Codes\Github\Digital-Image-Processing\XOR AND\im1.jpg'
image2_path = r'C:\Bijan\Codes\Github\Digital-Image-Processing\XOR AND\im2.jpg'

# image1_path = r'C:\Bijan\Codes\Github\Digital-Image-Processing\XOR AND\lena.webp'
# image2_path = r'C:\Bijan\Codes\Github\Digital-Image-Processing\XOR AND\taj.webp'

image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)


negative1 = 255 - image1
negative2 = 255 - image2

# Bitwise XOR operation
bitwise_xor = cv2.bitwise_xor(negative1, negative2)
bitwise_and = cv2.bitwise_and(negative1, negative2)

#plotting

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title('Image 1')
plt.imshow(image1, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Image 2')
plt.imshow(image2, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Bitwise XOR')
plt.imshow(bitwise_xor, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Bitwise AND')
plt.imshow(bitwise_and, cmap='gray')
plt.axis('off')

plt.tight_layout()

plt.show()