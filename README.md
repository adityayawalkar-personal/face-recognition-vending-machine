# face-recognition-vending-machine
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Recognition Based Vending Machine</title>
</head>
<body>

<h1>Face Recognition Based Vending Machine</h1>

<p>An intelligent vending machine system that uses facial recognition to identify users and dispenses items through Arduino-controlled hardware.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#hardware-requirements">Hardware Requirements</a></li>
    <li><a href="#software-requirements">Software Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#circuit-diagram">Circuit Diagram</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#future-enhancements">Future Enhancements</a></li>
    <li><a href="#contributing">Contributing</a></li>
</ul>

<h2 id="overview">Overview</h2>
<p>
    This project implements an automated vending machine that combines computer vision (face recognition)
    with Arduino-based hardware control. The system recognizes authorized users and dispenses items when 
    a hand is detected near the dispenser.
</p>

<h2 id="features">Features</h2>
<ul>
    <li><strong>Face Recognition</strong>: Identifies and authenticates users using computer vision</li>
    <li><strong>Contactless Dispensing</strong>: Uses ultrasonic sensor to detect hand placement</li>
    <li><strong>Automated Control</strong>: Arduino-controlled servo motor for item dispensing</li>
    <li><strong>Closed-Loop System</strong>: Continuous operation with Python-Arduino communication</li>
    <li><strong>Real-time Monitoring</strong>: Serial communication for system status updates</li>
</ul>

<h2 id="hardware-requirements">Hardware Requirements</h2>

<h3>Electronics Components</h3>
<ul>
    <li>Arduino Uno/Nano</li>
    <li>Ultrasonic Sensor HC-SR04</li>
    <li>Servo Motor SG90 or similar</li>
    <li>USB Cable</li>
    <li>Jumper Wires</li>
    <li>Breadboard (optional)</li>
    <li>Power Supply (5V)</li>
    <li>Webcam/USB Camera</li>
</ul>

<h3>Optional</h3>
<ul>
    <li>Machine enclosure</li>
    <li>LED indicators</li>
    <li>Buzzer</li>
</ul>

<h2 id="software-requirements">Software Requirements</h2>

<h3>Python Dependencies</h3>
<pre>
opencv-python
face-recognition
numpy
pyserial
</pre>

<h3>Arduino IDE</h3>
<ul>
    <li>Version 1.8.x or higher</li>
    <li>Servo library (default)</li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Step 1: Clone the Repository</h3>
<pre>
git clone https://github.com/yourusername/face-recognition-vending-machine.git
cd face-recognition-vending-machine
</pre>

<h3>Step 2: Install Python Dependencies</h3>
<pre>
pip install opencv-python face-recognition numpy pyserial
</pre>

<h3>Step 3: Upload Arduino Code</h3>
<ol>
    <li>Open <code>arduino_vending_machine.ino</code></li>
    <li>Select board & COM port</li>
    <li>Upload code</li>
</ol>

<h3>Step 4: Configure Python Script</h3>
<p>Update serial port:</p>
<pre>
arduino = serial.Serial('COM3', 9600)
</pre>
<p>Add face images into <code>known_faces/</code> and update encodings.</p>

<h2 id="circuit-diagram">Circuit Diagram</h2>

<pre>
Arduino Pin Connections:
├─ Pin 9  → Ultrasonic TRIG
├─ Pin 10 → Ultrasonic ECHO
├─ Pin 6  → Servo Signal
├─ 5V     → HC-SR04 & Servo
└─ GND    → HC-SR04 & Servo
</pre>

<h3>Ultrasonic Sensor HC-SR04</h3>
<ul>
    <li>VCC → 5V</li>
    <li>TRIG → 9</li>
    <li>ECHO → 10</li>
    <li>GND → GND</li>
</ul>

<h3>Servo Motor</h3>
<ul>
    <li>VCC → 5V</li>
    <li>GND → GND</li>
    <li>Signal → 6</li>
</ul>

<h2 id="how-it-works">How It Works</h2>

<h3>System Flow</h3>
<ol>
    <li>Face detection using webcam</li>
    <li>Face recognition using encodings</li>
    <li>Python sends <code>FACE_RECOGNIZED</code> to Arduino</li>
    <li>Ultrasonic detects hand</li>
    <li>Servo rotates 180° to dispense</li>
    <li>Servo resets</li>
    <li>System loops</li>
</ol>

<h3>Communication Protocol</h3>
<pre>
Python → Arduino: FACE_RECOGNIZED
Arduino → Python: ACK_FACE
Arduino → Python: HAND_DETECTED
Arduino → Python: DISPENSE_COMPLETE
</pre>

<h2 id="usage">Usage</h2>

<h3>Running the System</h3>
<ol>
    <li>Connect hardware</li>
    <li>Run Arduino code</li>
    <li>Start Python script:</li>
</ol>

<pre>
python face_recognition_vending.py
</pre>

<h3>Operation</h3>
<ul>
    <li>Look at the camera</li>
    <li>Wait for recognition</li>
    <li>Place hand near sensor</li>
    <li>Item dispenses</li>
</ul>

<h2>Configuration Options</h2>

<h3>Arduino</h3>
<pre>
#define DETECTION_DISTANCE 15
#define SERVO_DISPENSE_ANGLE 180
#define DISPENSE_DELAY 2000
</pre>

<h3>Python</h3>
<ul>
    <li>Camera index</li>
    <li>Face tolerance</li>
    <li>Serial port</li>
</ul>

<h2 id="known-issues">Known Issues</h2>
<ul>
    <li>Requires good lighting</li>
    <li>Servo may need external power</li>
    <li>Serial latency may vary</li>
</ul>

<h2 id="tips">Tips</h2>
<ul>
    <li>Use high-quality webcam</li>
    <li>Provide stable power</li>
    <li>Calibrate ultrasonic sensor</li>
    <li>Maintain organized face dataset</li>
</ul>

</body>
</html>
