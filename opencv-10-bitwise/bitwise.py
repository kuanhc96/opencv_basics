import numpy as np
import cv2

# canvas:
canvas = np.ones((300, 300), dtype="uint8") * 100 # when a 2D array is constructed, the values inside are in gray scale!

# rectangle:
rectangle = cv2.rectangle(canvas, (30, 30), (270, 270), (0, 0, 0), -1) # these drawing functions modify the input INPLACE!!!
cv2.imshow("rectangle", rectangle)

canvas = np.ones((300, 300), dtype="uint8") * 255
# circle:
circle = cv2.circle(canvas, (150, 150), 150, (0, 0, 0), -1)
cv2.imshow("circle", circle)

# The cv2.bitwise_and function will compare two values and treat the 0 like `False` and treat any other value as `True`
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwise_and)
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwise_or)
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwise_xor)

bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow("NOT rectangle", bitwise_not)
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("NOT circle", bitwise_not)
cv2.waitKey(0)