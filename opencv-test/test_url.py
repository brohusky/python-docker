import cv2

cap = cv2.VideoCapture('http://s3-ap-southeast-1.amazonaws.com/wm-production-storage/feed/4a807fbd-212a-4741-9622-7ca278f53135', cv2.CAP_FFMPEG)

print('cap: ', cap)

print('read: ', cap.read())