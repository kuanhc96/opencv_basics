import numpy as np
import cv2

canvas_width = 300
canvas_height = 300
canvas = np.zeros((canvas_height, canvas_width, 3), dtype="uint8")

canvas[:] = 255

cv2.imshow("canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.line(canvas, (0, canvas_width), (canvas_height, 0), blue, 5)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (canvas_height, canvas_width), green, 3)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)


grey = (128, 128, 128)
cv2.rectangle(canvas, (10, 25), (65, 45), grey, -1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

maroon = (0, 0, 128)
cv2.rectangle(canvas, (200, 150), (280, 280), maroon, 10)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

centerX = canvas_width // 2
centerY = canvas_height // 2
black = (0, 0, 0)

for radius in range (0, 150, 20):
    cv2.circle(canvas, (centerY, centerX), radius, black, 2)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)