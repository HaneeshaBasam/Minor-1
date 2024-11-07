import cv2

cap = cv2.VideoCapture(0)  # Change the index if necessary

if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
