import cv2
import matplotlib.pyplot as plt

img = cv2.imread("3.png", 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()