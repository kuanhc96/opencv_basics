import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="/Users/kuanhc96/Desktop/pyimagesearch/opencv-7-flipping/matt.jpg", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

print("[INFO] flip image horizontally")
flipped = cv2.flip(image, 1)
cv2.imshow("horizontal flip", flipped)

print("[INFO] flip image vertically")
flipped = cv2.flip(image, 0)
cv2.imshow("vertical flip", flipped)

print("[INFO] flip image around origin")
flipped = cv2.flip(image, -1)
cv2.imshow("flip around origin", flipped)
cv2.waitKey(0)