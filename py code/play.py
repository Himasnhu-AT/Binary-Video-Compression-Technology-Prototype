import cv2


video_path = "output.avi"

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Output", frame)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break

cv2.destroyAllWindows()
cap.release()
