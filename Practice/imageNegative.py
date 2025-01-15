import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigasit.jpg"

image = cv.imread(image_path, cv.COLOR_BGR2RGB)

#find the negative of the image
negative = 255 - image

plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(negative)
plt.title("Negative Image")
plt.axis('off')

plt.tight_layout()
plt.show()
