import cv2
import numpy as np
cap = cv2.VideoCapture('video.mkv')

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Set the start and end times for the clip (in seconds)
start_time = 30
end_time = 35

# Convert the start and end times to frames
start_frame = int(start_time * cap.get(cv2.CAP_PROP_FPS))
end_frame = int(end_time * cap.get(cv2.CAP_PROP_FPS))

  
# Read until video is completed
i=0
while(cap.isOpened()):
      
    # Capture frame-by-frame
    ret, frame = cap.read()
    # ret is a boolean variable that returns true if the frame is available.
    # frame is an image array vector captured based on the default frames per second defined explicitly or implicitly

    if ret == True :
    # Display the resulting frame

        #Resizing the frame
        frame = cv2.resize(frame, (0,0), fx = 0.6, fy = 0.6) #fx, fy are the scaling factors and tuple(0,0) is the output size

        # Get the frame dimensions
        height, width, _ = frame.shape


        # Creating a box at the centre of each frame
        if start_frame<=i and i<=end_frame:
            # Required box is placed at centre
            y = int(height/4)   #height of our box will be 2*y
            x = int(width/4)    #width of our box will be 2*x

            # Define the start, end points coordinates and color of the rectangle
            start_point = (x, y)    #Top-Left Corner
            end_point = (3*x, 3*y)  #Bottom-Right Corner
            box_color = (0, 0, 255)  # Red in BGR format

            #Creating a rectange
            cv2.rectangle(frame, start_point, end_point, box_color, 5)

        #Display
        cv2.imshow('Frame', frame)
        
          
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    i+=1
  
# When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()