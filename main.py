#ref https://github.com/keithweaver/python-aws-s3/blob/master/example.py

import cv2
import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = ''

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

print ("Initializing Image Upload...\n")

data = open(img_name, 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key=img_name, Body=data)

print ("Done")

