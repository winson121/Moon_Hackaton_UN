import cv2
import numpy as np
import imutils
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('test.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
frameSkip = 1
start = 0

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  if start == frameSkip:
    start = 0
    if ret == True:
      # Display the resulting frame
      frame = imutils.resize(frame, width=450)
      cv2.imshow('Frame',frame)

      print(type(frame))
      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Break the loop
    else:
      break
  else:
    start += 1

# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
