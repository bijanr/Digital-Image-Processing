# Perform Contrast Stretching for the purpose of image enhancement. Display the original image, the enhanced
# image, as well as their corresponding histograms respectively. (Refrain from using built-in functions e.g.,
# “normalization” in OpenCV to achieve the task).

import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretch(image):
    
    min_val = np.min(image)
    max_val = np.max(image)
    print(f"Original Min: {min_val}, Original Max: {max_val}")
    
    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    return stretched

def plot_histogram(image, title, ax):
    ax.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    ax.set_title(title)
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')


image_path = 'C:\\Bijan\\Codes\\Github\\Digital-Image-Processing\\images\\sky.jpg'  
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if original_image is None:
    print("Error: Image not found. Please check the image path.")
else:
    
    enhanced_image = contrast_stretch(original_image)

    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    
    axes[0, 0].imshow(original_image, cmap='gray')
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    
    plot_histogram(original_image, 'Original Image Histogram', axes[1, 0])

    
    axes[0, 1].imshow(enhanced_image, cmap='gray')
    axes[0, 1].set_title('Enhanced Image')
    axes[0, 1].axis('off')

    
    plot_histogram(enhanced_image, 'Enhanced Image Histogram', axes[1, 1])

    plt.tight_layout()
    plt.show()
