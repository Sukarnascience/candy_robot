# import the required modules
import cv2
import time
from deepface import DeepFace

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

# Initialize variables for FPS calculation
fps = 0
frame_count = 0
start_time = time.time()

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Initialize a list to store emotions
    emotions_list = []

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face from the frame
        face = frame[y:y + h, x:x + w]

        # Analyze the face for emotions
        result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)

        # Get the emotion with the highest score
        max_emotion = max(result[0]['emotion'], key=result[0]['emotion'].get)
        emotions_list.append(f"{max_emotion}: {result[0]['emotion'][max_emotion]:.2f}")

    # Calculate FPS
    frame_count += 1
    if time.time() - start_time >= 1:
        fps = frame_count
        frame_count = 0
        start_time = time.time()

    # Display emotions in the top left corner
    for i, emotion in enumerate(emotions_list):
        cv2.putText(frame, emotion, (10, 30 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Display FPS in the bottom left corner
    cv2.putText(frame, f'FPS: {fps}', (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Show the video feed with detected faces and emotions
    cv2.imshow('Video Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
