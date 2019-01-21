import cv2

cap = cv2.VideoCapture('./asset.jpeg', cv2.CAP_FFMPEG)

print('cap: ', cap)

print('read: ', cap.read())