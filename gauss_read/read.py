import numpy as np
import cv2 
import os 

image_path = '/data/GAUSS_32.png'
assert os.path.exists(image_path) and os.path.isfile(image_path) 

gauss = cv2.imread(image_path)

print(gauss)
print(f"MEAN SECOND:{np.mean(gauss)}")
