import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import pyautogui
from plyer import notification

# --- Configuration ---
SNOOP_THRESHOLD = 2  # Number of people allowed in frame
STRIKE_LIMIT = 3     # Consecutive frames with > threshold before action
COOLDOWN = 5         # Seconds to wait after an action is taken
MODEL_PATH = "blaze_face_short_range.tflite"

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
    # Initialize MediaPipe Face Detector (new Tasks API)
    base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.FaceDetectorOptions(
        base_options=base_options,
        min_detection_confidence=0.5
    )
    detector = vision.FaceDetector.create_from_options(options)

    cap = cv2.VideoCapture(0)
    strike_count = 0
    last_action_time = 0

    print("[*] AntiSnoop-AI is active. Press 'q' to stop.")

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Convert BGR (OpenCV) to RGB for MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

        # Run face detection
        detection_result = detector.detect(mp_image)

        # Count detected faces
        face_count = len(detection_result.detections)

        # Logic: If more than 1 person is seen
        if face_count >= SNOOP_THRESHOLD:
            strike_count += 1
            if strike_count >= STRIKE_LIMIT and (time.time() - last_action_time > COOLDOWN):
                trigger_security_action()
                last_action_time = time.time()
                strike_count = 0
        else:
            strike_count = 0

        # Draw bounding boxes on detected faces
        for detection in detection_result.detections:
            bbox = detection.bounding_box
            cv2.rectangle(image, 
                          (bbox.origin_x, bbox.origin_y),
                          (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height),
                          (0, 255, 0), 2)

        # UI Overlay (Optional: remove for 'Stealth Mode')
        cv2.putText(image, f"People: {face_count}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('AntiSnoop-AI Monitor', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    detector.close()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_antisnoop()
