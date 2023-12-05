import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/Users/kuanhc96/pyimagesearch/opencv-2/italian_girl.jpg", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2] # access the first two values (:2 means from 0 to 2, excluding 2) of image.shape, which is a tuple of 3 values representing h, w, c
print(h, w)
cv2.imshow("original italian", image)
cv2.waitKey(0)

(b, g, r) = image[0, 0]
print(f"pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")


(b, g, r) = image[910, 220]
print(f"pixel at (220, 910) - Red: {r}, Green: {g}, Blue: {b}")

(cX, cY) = (w // 2, h // 2)

top_left = image[0:cY, 0:cX]
cv2.imshow("top left", top_left)
cv2.waitKey(0)
top_right = image[0:cY, cX:]
cv2.imshow("top right", top_right)
bottom_left = image[cY:, 0:cX]
cv2.imshow("bottom left", bottom_left)
bottom_right = image[cY:, cX:]
cv2.imshow("bottom right", bottom_right)
cv2.waitKey(0)

image[cY:, :cX] = (128, 0, 128)
cv2.imshow("modified", image)
cv2.waitKey(0)