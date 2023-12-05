import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png", help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# the cv2.split method will split an image into its color components
(B, G, R) = cv2.split(image)

cv2.imshow("original", image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)

# The following merge/stack methods achieved the same output array
bgr_numpy = np.dstack([B, G, R])
merged = cv2.merge([B, G, R])
print(merged.shape)
print(bgr_numpy.shape)
print(type( merged ))
print(type( bgr_numpy ))
cv2.imshow("Merged", merged)

zeros = np.zeros(image.shape[:2], dtype="uint8")
blue_channel = cv2.merge([B, zeros, zeros])
green_channel = cv2.merge([zeros, G, zeros])
red_channel = cv2.merge([zeros, zeros, R])
cv2.imshow("BLUE", blue_channel)
cv2.imshow("GREEN", green_channel)
cv2.imshow("RED", red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()