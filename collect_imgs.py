import os
import cv2

DATA_DIR = './data'

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Initialize video capture (camera index might need to be adjusted)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

for j in range(number_of_classes):
    # Create directory for each class if it doesn't exist
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    # First, display the ready message
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image")
            break

        # Display the "Ready" message
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Now collect and save images
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image")
            break

        # Display the current frame
        cv2.imshow('frame', frame)

        # Save the frame as an image
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)

        print(f"Saved image {counter + 1}/{dataset_size} for class {j}")

        counter += 1

        # Introduce a small delay to prevent capturing too quickly
        if cv2.waitKey(100) & 0xFF == ord('q'):  # Adjust delay as needed
            break

cap.release()
cv2.destroyAllWindows()
