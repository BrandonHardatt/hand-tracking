import cv2
import mediapipe as mp

# Initialize Mediapipe's hand tracking module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the webcam feed
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    # Convert the frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with Mediapipe
    results = hands.process(rgb_frame)
    
    # If hands are detected, draw landmarks on the frame
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for landmark in landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
    
    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    
    # Exit the prograqm if q is pressed 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
