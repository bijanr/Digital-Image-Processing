import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'C:\Bijan\Codes\Github\Digital-Image-Processing\images\sky.jpg'
image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)

if image is None:
    print("Error: Image not found. Please check the image path.")
    exit()
negative_image = 255 - image


watermark_text = "Shot on RealMe C67 5G"
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 6
font_thickness = 5


watermark = np.zeros_like(image, dtype=np.uint8)
gap_from_bottom = 100 
text_size = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
text_x = (watermark.shape[1] - text_size[0]) // 2  
text_y = watermark.shape[0] - gap_from_bottom  



cv2.putText(watermark, watermark_text, (text_x, text_y), font, font_scale, 255, font_thickness)


watermarked_image = cv2.addWeighted(negative_image, 1, watermark, 0.3, 0)


fig, axes = plt.subplots(2, 2, figsize=(12, 10))


axes[0, 0].imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("Original Image")
axes[0, 0].axis('off')

axes[1, 0].hist(image.ravel(), bins=256, range=(0, 256), color='blue')
axes[1, 0].set_title("Histogram of Original Image")


axes[0, 1].imshow(watermarked_image, cmap='gray')
axes[0, 1].set_title("Watermarked Negative Image")
axes[0, 1].axis('off')

axes[1, 1].hist(watermarked_image.ravel(), bins=256, range=(0, 256), color='red')
axes[1, 1].set_title("Histogram of Watermarked Image")

plt.tight_layout()
plt.show()
