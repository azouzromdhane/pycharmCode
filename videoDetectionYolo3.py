import cv2

# Initialize webcam
cap = cv2.VideoCapture("building.mp4")

while True:
    # Read first frame
    ret, frame1 = cap.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Read next frame
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate difference between frames
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference to identify motion
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the dilated image
    cnts, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame
    for c in cnts:
        if cv2.contourArea(c) < 2500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('OBJECT DETECTED'), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                    3)
    cv2.putText(frame1, "Status: {}".format('Press Q to exit'), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (215, 10, 10), 3)

    # Show the frame
    cv2.imshow("Motion Detection", frame1)

    # Update the previous frame
    gray1 = gray2

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()