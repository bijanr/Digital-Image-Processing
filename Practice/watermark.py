import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = 'C:\Bijan\Codes\Github\Digital-Image-Processing\images\sky.jpg'
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found. Please check the image path.")
    exit()

watermark_text = "Shot on RealMe C67 5G"
font = cv.FONT_HERSHEY_DUPLEX
font_scale = 6
font_thickness = 5

watermark = np.zeros_like(image, dtype=np.uint8) #demo watermark mask

gap = 100
text_size = cv.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
x_align = (watermark.shape[1] - text_size[0]) // 2
y_align = (watermark.shape[1] - gap)

cv.putText(watermark, watermark_text, (x_align, y_align), font, font_scale, 255, font_thickness)

watermarked_image = cv.addWeighted(image, 1, watermark, 0.5, 0)


