import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk

# Load the trained YOLOv8 model
model = YOLO(r'/home/alperen/Desktop/CAT-DETECTION-1/best1.pt')  # Adjust the path to your trained model

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or specify the webcam index

def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    # Perform inference
    results = model.predict(frame)

    # Annotate the frame with detection results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Extract bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"
            
            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw label
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Convert the frame to an ImageTk object
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the label with the new image
    lbl.imgtk = imgtk
    lbl.configure(image=imgtk)

    # Schedule the next update
    lbl.after(10, update_frame)


# Create the main window
root = tk.Tk()
root.title("Webcam Detection")

# Create a label to display the video feed
lbl = tk.Label(root)
lbl.pack()

# Start the video feed
update_frame()

# Start the Tkinter event loop
root.mainloop()

# Release the webcam
cap.release()