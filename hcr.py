import cv2
import mediapipe as mp
import pyautogui
import keyboard  # type: ignore # New import for better key handling

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start video capture
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    """Count extended fingers using landmark positions."""
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    finger_tips = [8, 12, 16, 20]
    finger_bottoms = [6, 10, 14, 18]

    for tip, bottom in zip(finger_tips, finger_bottoms):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[bottom].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)  # Count extended fingers

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame horizontally for natural movement
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand tracking
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get finger count
            finger_count = count_fingers(hand_landmarks)

            if finger_count == 0:  # Closed fist (Brake)
                keyboard.release("right")  # Ensure gas is released
                keyboard.press("left")  # Press brake
                print("Brake Pressed")
            elif finger_count == 5:  # All fingers extended (Gas)
                keyboard.release("left")  # Ensure brake is released
                keyboard.press("right")  # Press gas
                print("Gas Pressed")
            else:
                # Release both keys if no specific gesture is detected
                keyboard.release("right")
                keyboard.release("left")

    # Display the frame
    cv2.imshow("Hand Control", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
