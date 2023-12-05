import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="/Users/kuanhc96/Desktop/pyimagesearch/opencv-3-drawing/beach_day.jpg", help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
red = (0, 0, 255)
right_click_history = []
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN or flags == cv2.EVENT_FLAG_LBUTTON:
        print("CLICK")
        cv2.circle(image, (x, y), 50, red, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        (b, g, r) = image[y, x]
        print(f"pixel at {y}, {x} has an RGB value of ({r}, {g}, {b})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        param.append((x, y))
        cv2.circle(image, (x, y), 10, red, -1)
        if len(param) > 1:
            cv2.line(image, param[-2], param[-1], red, 10)


cv2.namedWindow('beach day')
# parameters: 'image' -> refers to the "named window"; get_pixel -> the function that cv2 will call
# flags-> used for the "flag events" such as dragging; param -> used when some object needs to be passed to the event listener
cv2.setMouseCallback('beach day', draw_circle, right_click_history) 

while(1):
    cv2.imshow('beach day', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()