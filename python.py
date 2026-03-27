import cv2
import mediapipe as mp
import time
import pyautogui
from plyer import notification

# --- Configuration ---
SNOOP_THRESHOLD = 2  # Number of people allowed in frame
STRIKE_LIMIT = 3     # Consecutive frames with > threshold before action
COOLDOWN = 5         # Seconds to wait after an action is taken

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

def trigger_security_action():
    """Action taken when unauthorized onlookers are detected."""
    notification.notify(
        title="Snoop Alert!",
        message="Unauthorized person detected. Locking screen...",
        timeout=2
    )
    # On Windows: pyautogui.hotkey('win', 'l')
    # On Linux (Ubuntu/GNOME): 
    # import os; os.system('gnome-screensaver-command -l')
    print("[!] SECURITY BREACH: Locking/Minimizing Windows...")
    pyautogui.hotkey('win', 'd') # Minimizes all windows to hide work

def run_antisnoop():
    cap = cv2.VideoCapture(0)
    strike_count = 0
    last_action_time = 0

    print("[*] AntiSnoop-AI is active. Press 'q' to stop.")

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Convert to RGB for MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        # Count detected faces
        face_count = 0
        if results.detections:
            face_count = len(results.detections)

        # Logic: If more than 1 person is seen
        if face_count >= SNOOP_THRESHOLD:
            strike_count += 1
            if strike_count >= STRIKE_LIMIT and (time.time() - last_action_time > COOLDOWN):
                trigger_security_action()
                last_action_time = time.time()
                strike_count = 0
        else:
            strike_count = 0

        # UI Overlay (Optional: remove for 'Stealth Mode')
        cv2.putText(image, f"People: {face_count}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('AntiSnoop-AI Monitor', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_antisnoop()
