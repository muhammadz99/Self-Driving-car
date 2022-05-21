import cv2
vidcap = cv2.VideoCapture('drivingVideo.mp4')
success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite("%d.jpg" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1
