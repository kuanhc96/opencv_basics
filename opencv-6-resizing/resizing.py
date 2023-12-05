# tutorial: https://pyimagesearch.com/2021/01/20/opencv-resize-image-cv2-resize/?_ga=2.20892728.1862556207.1701016519-1842902230.1698424416
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/Users/kuanhc96/Desktop/pyimagesearch/opencv-6-resizing/alice_and_i.jpeg", help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

ratio = 0.1
print(image.shape) # height * width
new_width = int( image.shape[1] * ratio )
new_height = int( image.shape[0] * ratio )
new_dim = (new_width, new_height)
print(new_dim)
resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA) # The new dimensions are expressed by (width * height). This ordering is different from the numpy shape
cv2.imshow("resized by tenth", resized)
cv2.imwrite("/Users/kuanhc96/Desktop/pyimagesearch/opencv-6-resizing/tenth_matt.jpg", resized)

resized = imutils.resize(image, width=1000)
print(resized.shape)
cv2.imshow("resized with imutils", resized)

image = cv2.imread("/Users/kuanhc96/Desktop/pyimagesearch/opencv-6-resizing/tenth_matt.jpg")
# resizing algorithms:
# 1. INTER_NEAREST: fastest, but least accurate. Simply takes the nearest neighbor and uses it for interpolation
# 2. INTER_LINEAR: fast, but less accurate. Uses a linear function (i.e., y = mx + b) to interpolate
# 3. INTER_AREA: balanced accuracy and speed. For info, read https://medium.com/@wenrudong/what-is-opencvs-inter-area-actually-doing-282a626a09b3
# 4. INTER_CUBIC: slow, but more accurate. Uses a cubic function for interpolation
# 5. INTER_LANCZOS4: slowest, but most accurate. Rarely used in practive. Uses a sinusoidal interpolation method
methods = [
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_AREA", cv2.INTER_AREA),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4),
]

for (name, method) in methods:
    print(f"[INO] {name}")
    resized = imutils.resize(image, width=1000, inter=method)
    cv2.imshow(f"Method: {name}", resized)

cv2.waitKey(0)