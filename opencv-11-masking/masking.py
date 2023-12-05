import numpy as np
# I = np.arange(0, 25)
# print(I)

# I = I.reshape((5,5))
# print(I)
# print(I[:3, :2])
# print(I[3:, 1:])

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="alice_turning.jpeg", help="path to image")
args = vars( ap.parse_args() )

image = cv2.imread(args["image"])
cv2.imshow("original", image)

#rectangle face mask
mask = np.zeros(image.shape[:2], dtype="uint8")
# bounding box: WxH: 614x716
bounding_box_height = 716
bounding_box_width = 614
cv2.rectangle(mask, (1265, 1790), ( 1265+bounding_box_width, 1790+bounding_box_height), 255, -1) # rectange points are specified using (x, y) coordinates
cv2.imshow("mask", mask)
print(mask.shape)
print(image.shape)
alice_face = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Alice's face", alice_face)

# circle mask
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (1265 + bounding_box_width // 2, 1790 + bounding_box_height // 2)
cv2.circle(mask, (cX, cY), bounding_box_height // 2, 255, -1) # rectange points are specified using (x, y) coordinates
cv2.imshow("mask", mask)
alice_face = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Alice's face", alice_face)

mask = np.zeros(image.shape[:2], dtype="uint8")
# body bounding box: W:1405 H:4292
bounding_box_height = 4292
bounding_box_width = 1405
cv2.rectangle(mask, (1000, 1790), ( 1000 + bounding_box_width, 1790 + bounding_box_height), 255, -1) # rectange points are specified using (x, y) coordinates
alice_body = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Alice's body", alice_body)


cv2.waitKey(0)