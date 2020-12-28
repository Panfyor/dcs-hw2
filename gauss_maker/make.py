import numpy as np
import cv2 
import os


image_path = 'Lenna_(test_image).png'
assert os.path.exists(image_path) and os.path.isfile(image_path) 
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


print("Original Image 32x32")
img = cv2.resize(img, (32,32))
print(img)

print("Gauss 32x32")
gauss = cv2.GaussianBlur(img, (21,21), 0)
print(gauss)


print(f"MEAN FIRST:{np.mean(gauss)}")
cv2.imwrite("/data/GAUSS_32.png", gauss)
