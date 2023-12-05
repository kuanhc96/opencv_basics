import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="kissing.jpeg", help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # images are numpy arrays stored as unsigned 8-bit integers (uint8)
# the range of legal values for 8-bit integers is from 0 - 255. 
# opencv and numpy have different methods of handling values that go beyond or below these bounds:
# OpenCV: the value will cap at 0 and 255. 
# numpy: the value will "wrap around" (modulus operation will be taken)
cv2.imshow("Original", image)
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([100]), np.uint8([200]))
print(f"cv2 max: {added}")
print(f"cv2 min: {subtracted}")

added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([100]) - np.uint8([200])
print(f"numpy max: {added}")
print(f"numpy min: {subtracted}")

filter = np.ones(image.shape, dtype="uint8") * 100
filtered_image = image + filter
cv2.imshow("filtered image (numpy add)", filtered_image)

filter = np.ones(image.shape, dtype="uint8") * 100
filtered_image = image - filter
cv2.imshow("filtered image (numpy subtract)", filtered_image)

filter = np.ones(image.shape, dtype="uint8") * 100
filtered_image = cv2.add(image, filter)
cv2.imshow("filtered image (opencv add)", filtered_image)

filter = np.ones(image.shape, dtype="uint8") * 100
filtered_image = cv2.subtract(image, filter)
cv2.imshow("filtered image (opencv subtract)", filtered_image)
cv2.waitKey(0)