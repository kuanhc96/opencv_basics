import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
#print(ap.parse_args()) # ap.parse_args() returns a `namespace` object 
args = vars(ap.parse_args()) # args is a dictionary
# print(args)

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]
print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(f"channels: {c}")

cv2.imshow("Matt and Kuan", image)
cv2.waitKey(0)

cv2.imwrite("matt_and_i.jpg", image)