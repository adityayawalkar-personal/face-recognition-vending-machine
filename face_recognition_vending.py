import cv2
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import serial
import time
import numpy as np

# Initialize serial connection with Arduino
arduino = serial.Serial('COM11', 9600, timeout=1)
time.sleep(2)

# Load face recognition model (replace with your trained model)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#known_faces = {'Aditya Yawalkar': "C:\Users\Aditya\Downloads\iloveimg-converted\IMG20231229172825.jpg", "Abdur Rahman Khan": "C:\Users\Aditya\Downloads\iloveimg-converted\Abdur (6).jpg", "Advaith Ajithkumar": "C:\Users\Aditya\Downloads\iloveimg-converted\Advaith_Smile (113).jpg", "Amarpreet Singh Chaman": "C:\Users\Aditya\Downloads\iloveimg-converted\Amar_Normal (35).jpg"}
known_faces = {
    "Aditya Yawalkar": r"C:\Users\Aditya\Downloads\iloveimg-converted\IMG20231229172825.jpg",
    "Abdur Rahman Khan": r"C:\Users\Aditya\Downloads\iloveimg-converted\Abdur (6).jpg",
    "Advaith Ajithkumar": r"C:\Users\Aditya\Downloads\iloveimg-converted\Advaith_Smile (113).jpg",
    "Amarpreet Singh Chaman": r"C:\Users\Aditya\Downloads\iloveimg-converted\Amar_Normal (35).jpg"
}

def recognize_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        # Compare with known faces (simplified)
        for name, img_path in known_faces.items():
            known_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if np.mean(roi_gray) - np.mean(known_img) < 10:  # Simple threshold comparison
                return name
    return "Face not recognized"

def capture_image():
    ret, frame = cap.read()
    if ret:
        name = recognize_face(frame)
        label_name.config(text=f"Name: {name}")
        if name != "Face not recognized":
            label_sensor.config(text="Put your hand near the sensor")
            arduino.write(b'1')  # Send signal to Arduino

# GUI Setup
root = tk.Tk()
root.title("Face Recognition System")
root.geometry("600x500")

label_title = Label(root, text="Face Recognition System", font=("Arial", 16))
label_title.pack()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

label_name = Label(root, text="Name: --", font=("Arial", 14))
label_name.pack()

label_sensor = Label(root, text="", font=("Arial", 12))
label_sensor.pack()

button_capture = Button(root, text="Capture Image", command=capture_image)
button_capture.pack()

# Video Capture
cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        canvas.imgtk = imgtk
    root.after(10, update_frame)

update_frame()
root.mainloop()

# Close resources
cap.release()
cv2.destroyAllWindows()
