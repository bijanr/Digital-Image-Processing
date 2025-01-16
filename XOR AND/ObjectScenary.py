import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Define paths to the image and object
image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\nigajit2.jpg"
object_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\jail.png"

# Read the images
image = cv.imread(image_path)
object = cv.imread(object_path)

# Convert images to RGB (as OpenCV reads in BGR format)
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
object = cv.cvtColor(object, cv.COLOR_BGR2RGB)

# Define region of interest with top-left (x_offset, y_offset) and a width and height
x_offset = 0
y_offset = 0
width, height = image.shape[1], image.shape[0]

# Resize the object to match the size of the region of interest
object_resized = cv.resize(object, (image.shape[1], image.shape[0]))



# Display the images using subplots
plt.subplot(2, 3, 1)
plt.imshow(cv.cvtColor(cv.imread(image_path), cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(object_resized)
plt.title("Resized Object")
plt.axis("off")


plt.subplot(2, 3, 3)
plt.imshow(image)
plt.title("Final Image (Object Added)")
plt.axis("off")

plt.tight_layout()
plt.show()
