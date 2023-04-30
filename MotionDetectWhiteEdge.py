import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the frame size
cap.set(3, 640)
cap.set(4, 480)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# Read the first frame
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set a threshold for the difference between frames
threshold = 25

while True:
    # Read a new frame
    ret, frame = cap.read()

    # Convert the new frame to grayscale
    gray_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the two frames
    difference = cv2.absdiff(gray, gray_new)

    # Threshold the difference to identify changes
    threshold_difference = cv2.threshold(difference, threshold, 255, cv2.THRESH_BINARY)[1]

    # Check if there is motion
    if cv2.countNonZero(threshold_difference) > 0:
        # If there is motion, write the frame to the video file
        out.write(frame)

    # Update the grayscale frame
    gray = gray_new

    # Display the difference frame
    cv2.imshow("Difference", threshold_difference)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter object
out.release()

# Release the webcam
cap.release()

# Destroy all windows
cv2.destroyAllWindows()

# updated version of the code that continues to capture motion until the user interrupts with the keyboard. This code will continue to capture motion indefinitely, until the user presses the 'q' key to exit the loop.
