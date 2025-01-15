import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # histogram calculation
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

    # intensity wise probabilistic analysis
    pdf = hist / hist.sum()

    # Cumulative Distribution Function (CDF)
    cdf = pdf.cumsum()
    cdf_min = cdf[cdf > 0].min()  # Minimum non-zero CDF value

    # normization of CDF
    cdf_normalized = ((cdf - cdf_min) / (1 - cdf_min) * 255).astype(np.uint8)

    # mapping original image with modified cdf
    equalized_image = cdf_normalized[image]

    return equalized_image, hist, cdf_normalized

def plot_histogram(image, title, ax):
    ax.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    ax.set_title(title)
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')


image_path = r"C:\Bijan\Codes\Github\Digital-Image-Processing\Practice\ref\hansleep.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if original_image is None:
    print("Error: Image not found. Please check the image path.")
else:
    equalized_image, original_hist, equalized_hist = histogram_equalization(original_image)

    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    
    axes[0, 0].imshow(original_image, cmap='gray')
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    
    plot_histogram(original_image, 'Original Image Histogram', axes[1, 0])

    
    axes[0, 1].imshow(equalized_image, cmap='gray')
    axes[0, 1].set_title('Enhanced Image')
    axes[0, 1].axis('off')


    plot_histogram(equalized_image, 'Equalized Image Histogram', axes[1, 1])

    plt.tight_layout()
    plt.show()
