# 🐱 Smart Pet Feeder with Custom Cat Recognition (Edge Computer Vision)

An automated, IoT-enabled smart pet feeding system powered by computer vision. The system ensures that **only a specific, authorized cat** is fed—preventing stray animals or other pets from triggering food dispensing—while enforcing daily feeding limits and sending real-time email notifications to the owner.

---

## ⚙️ How It Works (End-to-End Pipeline)

1. **Motion Trigger:** A PIR motion sensor (`motion_sensor.py` / `motion2.py`) continuously monitors the feeding area in low-power standby mode.
2. **Camera Activation & Inference:** Once motion is detected, the camera wakes up and runs real-time object detection (`detect.py`) using a custom-trained YOLO model (`best.pt`).
3. **Identity Verification & Daily Quota Check:**
   - **Authorized Cat Detected:** If the detected target matches the specific cat and the daily limit (**maximum 3 feedings per day**) has not been reached, the system triggers the dispensing mechanism.
   - **Unauthorized Target / Limit Reached:** If another cat, a different object, or a false trigger is detected—or if the daily 3-meal quota is full—the dispenser remains locked.
4. **Actuation (Servo Control):** A servo motor (`servo_sens.py` / `servo2.py`) rotates to release a controlled portion of food into the bowl.
5. **Automated Email Alerts:** Immediately after a feeding event (or notable detection activity), the system sends a detailed email report with timestamps and daily feeding count directly to the owner.

---

## 🚀 Key Features

- **Custom Object Detection:** Trained on a custom-labeled dataset (via Roboflow) to distinguish a specific cat from other animals and background objects.
- **Hardware-in-the-Loop Automation:** Seamless integration between PIR motion sensors, camera module, and servo actuators.
- **Overfeeding Protection:** Built-in daily scheduler/counter restricting food dispensing to a maximum of **3 times per day**.
- **Real-Time Owner Notifications:** Automated SMTP email alerts providing feeding logs and status updates.
- **Event-Driven Efficiency:** Camera inference runs only upon motion detection rather than continuous 24/7 streaming.

---

## 📂 Repository Structure

```text
├── train/                  # Training images and YOLO annotations
├── valid/                  # Validation dataset
├── test/                   # Test dataset
├── data.yaml               # Dataset configuration and class definitions
├── best.pt / best1.pt      # Trained YOLO model weights
├── detect.py               # Main computer vision inference & decision logic
├── motion_sensor.py        # PIR motion sensor trigger script
├── motion2.py              # Secondary/updated motion handling module
├── servo_sens.py           # Integrated sensor-to-servo control script
├── servo2.py               # Servo motor actuation module
└── README.roboflow.txt     # Dataset export metadata
```

---

## 🛠️ Tech Stack

- **Language:** Python
- **Computer Vision & Deep Learning:** PyTorch, YOLO (Ultralytics), OpenCV, Roboflow
- **Hardware & IoT:** PIR Motion Sensor, Camera Module, Servo Motor (GPIO control)
- **Notifications:** Python `smtplib` / Email Automation

---

## 🔧 Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alperen4066/CAT-DETECTION-.git
   cd CAT-DETECTION-
   ```

2. **Install dependencies:**
   ```bash
   pip install ultralytics opencv-python torch
   # Install hardware-specific GPIO libraries (e.g., RPi.GPIO or gpiozero) on your edge device
   ```

3. **Configure Email & Hardware Pins:**
   - Update your sender/receiver email credentials and SMTP settings in the notification configuration.
   - Verify GPIO pin mappings for the PIR motion sensor and servo motor in `servo_sens.py` and `detect.py`.

4. **Run the system:**
   ```bash
   python detect.py
   ```
