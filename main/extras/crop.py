import cv2
cap = cv2.VideoCapture("C:\\Users\\91638\\Videos\\ScreenRecorderFiles\\20220803\\01-04-42.mp4")
# Read until video is completed

writer = cv2.VideoWriter('sample.mp4',cv2.VideoWriter_fourcc(*'mp4v'),10,(910, 800))
#out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (910,800))
i=0
while(cap.isOpened()):
  # Capture frame-by-frame
    ret, frame = cap.read()
    frame = frame[0:800, 0:910]
    i+=1
    if(i>50):
        writer.write(frame)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
  
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
# When everything done, release 
# the video capture object
writer.release()

cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()