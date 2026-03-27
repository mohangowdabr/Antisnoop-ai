AntiSnoop-AI 🛡️
AntiSnoop-AI is a real-time privacy protection tool built with Python. It uses Computer Vision to monitor your workstation's surroundings via the webcam and automatically secures your session if an unauthorized onlooker (shoulder surfer) is detected.
🚀 Features
 * Real-time Face Detection: Monitors the number of people in the camera frame.
 * Intruder Alerts: Triggers desktop notifications when more than one person is detected.
 * Auto-Lock System: Automatically locks your workstation or minimizes windows if a "snoop" persists for more than 2 seconds.
 * Low Latency: Optimized for modern hardware like the Lenovo LOQ using OpenCV and MediaPipe.
 * Privacy First: All processing is done locally on your machine; no video data is ever uploaded or stored.
🛠️ Tech Stack
 * Language: Python 3.x
 * Vision: OpenCV & MediaPipe
 * Automation: PyAutoGUI & OS-level commands
 * Notifications: Plyer
📋 Prerequisites
Ensure you have Python installed, then install the required dependencies:
pip install opencv-python mediapipe pyautogui plyer

🔧 Installation & Usage
 * Clone the repository:
   git clone https://github.com/MohanGowda/AntiSnoop-AI.git
cd AntiSnoop-AI

 * Run the application:
   python main.py

 * Configuration:
   You can adjust the SNOOP_THRESHOLD (number of faces) and LOCK_TIMEOUT in the config.py file to suit your environment.
📂 Project Structure
 * main.py: The entry point for the application and camera loop.
 * detector.py: Contains the logic for face detection and counting.
 * actions.py: Handles system-level responses (locking, blurring, or alerting).
 * config.py: Global settings for sensitivity and timeouts.
🤝 Contributing
Contributions are welcome! If you're a fellow CSE student or developer, feel free to fork this repo and submit a pull request with new features (like gaze detection or GPU acceleration).
Author
Mohan Gowda B.Tech CSE Student | Cybersecurity Enthusiast
