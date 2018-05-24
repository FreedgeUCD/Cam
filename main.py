#ref https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

import cv2

cam = cv2.VideoCapture(1)

cv2.namedWindow("test")

img_counter = 0


ret, frame = cam.read()
cv2.imshow("test", frame)
k = cv2.waitKey(1)

img_name = "opencv_frame_{}.png".format(img_counter)
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))
img_counter += 1

cam.release()

cv2.destroyAllWindows()