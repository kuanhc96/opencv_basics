import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/Users/kuanhc96/Desktop/pyimagesearch/opencv-4-translation/alice_and_janet.jpeg", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("original alice and janet", image)
# positive tx: shift right
# positive ty: shift down
# negative tx: shift left
# negative ty: shift down
tx = -1000
ty = 500
# the identity matrix:
# [
#     [1, 0]
#     [0, 1]
# ]
# will preserve the original matrix. Tweaking the entries in this matrix will warp the matrix
# the first and fourth entries will enlarge or shrink the matrix by a certain factor along the x and y axes;
# the second and third entries will twist the image
M = np.float32(
[ 
    [1, 0, tx],
    [0, 1, ty]
 ]
)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("translated alice and janet", shifted)

shifted = imutils.translate(image, 0, 1000)
cv2.imshow("translated alice and janet 2", shifted)
cv2.waitKey(0)