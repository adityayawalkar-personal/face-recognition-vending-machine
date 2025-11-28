# face-recognition-vending-machine
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Face Recognition Based Vending Machine</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#9aa4b2;
      --accent:#60a5fa;
      --glass: rgba(255,255,255,0.03);
      --radius:12px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      color-scheme: dark;
    }

    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071021 0%, #071725 60%);color:#e6eef6;}
    .container{max-width:980px;margin:36px auto;padding:28px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border-radius:var(--radius);box-shadow:0 8px 30px rgba(2,6,23,0.7);}
    header{display:flex;align-items:center;gap:16px;margin-bottom:20px;}
    h1{font-size:1.8rem;margin:0}
    .subtitle{color:var(--muted);font-size:0.95rem}
    nav.toc{background:var(--glass);padding:14px;border-radius:10px;margin:18px 0;}
    nav.toc h2{font-size:1rem;margin:0 0 10px 0}
    nav.toc ul{margin:0;padding-left:18px;color:var(--muted)}
    nav.toc a{color:var(--accent);text-decoration:none}
    section{margin:20px 0;padding:16px;background:rgba(255,255,255,0.01);border-radius:10px}
    h2.section-title{margin-top:0}
    ul,ol{line-height:1.6}
    .code-block{background:#071427;border:1px solid rgba(255,255,255,0.03);padding:12px;border-radius:8px;overflow:auto;font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;font-size:0.95rem;color:#dbeafe}
    .inline-code{background:rgba(255,255,255,0.03);padding:2px 6px;border-radius:6px;font-family:ui-monospace,monospace}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
    .card{padding:12px;border-radius:10px;background:rgba(255,255,255,0.01);box-shadow:inset 0 -1px 0 rgba(255,255,255,0.01)}
    footer{font-size:0.9rem;color:var(--muted);margin-top:18px;text-align:center}
    .note{color:var(--muted);font-size:0.95rem}
    pre{margin:0}
    /* responsive tweaks */
    @media (max-width:640px){
      header{flex-direction:column;align-items:flex-start;gap:8px}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <h1>Face Recognition Based Vending Machine</h1>
        <div class="subtitle">An intelligent vending machine system that uses facial recognition to identify users and dispenses items through Arduino-controlled hardware.</div>
      </div>
    </header>

    <!-- Table of Contents -->
    <nav class="toc" aria-label="Table of contents">
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
        <li><a href="#license">License</a></li>
      </ul>
    </nav>

    <!-- Overview -->
    <section id="overview">
      <h2 class="section-title">Overview</h2>
      <p>This project implements an automated vending machine that combines computer vision (face recognition) with Arduino-based hardware control. The system recognizes authorized users through facial recognition and dispenses items when a hand is detected near the dispenser.</p>
    </section>

    <!-- Features -->
    <section id="features">
      <h2 class="section-title">Features</h2>
      <ul>
        <li><strong>Face Recognition</strong>: Identifies and authenticates users using computer vision</li>
        <li><strong>Contactless Dispensing</strong>: Uses ultrasonic sensor to detect hand placement</li>
        <li><strong>Automated Control</strong>: Arduino-controlled servo motor for item dispensing</li>
        <li><strong>Closed-Loop System</strong>: Continuous operation with Python–Arduino communication</li>
        <li><strong>Real-time Monitoring</strong>: Serial communication for system status updates</li>
      </ul>
    </section>

    <!-- Hardware Requirements -->
    <section id="hardware-requirements">
      <h2 class="section-title">🔧 Hardware Requirements</h2>

      <div class="grid">
        <div class="card">
          <h3>Electronics Components</h3>
          <ul>
            <li>Arduino Uno/Nano (1x)</li>
            <li>Ultrasonic Sensor HC-SR04 (1x)</li>
            <li>Servo Motor SG90 or similar (1x)</li>
            <li>USB Cable for Arduino (1x)</li>
            <li>Jumper Wires</li>
            <li>Breadboard (optional)</li>
            <li>Power Supply (5V for Arduino and servo)</li>
            <li>Webcam/USB Camera (for face recognition)</li>
          </ul>
        </div>

        <div class="card">
          <h3>Optional</h3>
          <ul>
            <li>Enclosure/Chassis for vending machine</li>
            <li>LED indicators</li>
            <li>Buzzer for audio feedback</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Software Requirements -->
    <section id="software-requirements">
      <h2 class="section-title">Software Requirements</h2>

      <h3>Python Dependencies</h3>
      <div class="code-block" aria-label="Python dependencies">
<pre><code>opencv-python
face-recognition
numpy
pyserial</code></pre>
      </div>

      <h3 style="margin-top:12px;">Arduino IDE</h3>
      <ul>
        <li>Version 1.8.x or higher</li>
        <li>Servo library (included by default)</li>
      </ul>
    </section>

    <!-- Installation -->
    <section id="installation">
      <h2 class="section-title">Installation</h2>

      <h3>Step 1: Clone the Repository</h3>
      <div class="code-block">
<pre><code>git clone https://github.com/yourusername/face-recognition-vending-machine.git
cd face-recognition-vending-machine</code></pre>
      </div>

      <h3 style="margin-top:12px;">Step 2: Install Python Dependencies</h3>
      <div class="code-block">
<pre><code>pip install opencv-python face-recognition numpy pyserial</code></pre>
      </div>

      <h3 style="margin-top:12px;">Step 3: Upload Arduino Code</h3>
      <ol>
        <li>Open <span class="inline-code">arduino_vending_machine.ino</span> in Arduino IDE</li>
        <li>Select your board (Tools → Board → Arduino Uno/Nano)</li>
        <li>Select the correct COM port (Tools → Port)</li>
        <li>Click Upload</li>
      </ol>

      <h3 style="margin-top:12px;">Step 4: Configure Python Script</h3>
      <ol>
        <li>Update the serial port in the Python script:
          <div class="code-block">
<pre><code>arduino = serial.Serial('COM3', 9600)  # Change COM3 to your port</code></pre>
          </div>
        </li>
        <li>Add face images to the <span class="inline-code">known_faces/</span> directory</li>
        <li>Update face encodings in the script</li>
      </ol>
    </section>

    <!-- Circuit Diagram -->
    <section id="circuit-diagram">
      <h2 class="section-title">Circuit Diagram</h2>

      <div class="code-block">
<pre><code>Arduino Pin Connections:
├─ Pin 9  → Ultrasonic Sensor (TRIG)
├─ Pin 10 → Ultrasonic Sensor (ECHO)
├─ Pin 6  → Servo Motor (Signal)
├─ 5V     → Ultrasonic Sensor (VCC) & Servo (VCC)
└─ GND    → Ultrasonic Sensor (GND) & Servo (GND)</code></pre>
      </div>

      <h3 style="margin-top:12px;">Connection Details</h3>
      <ul>
        <li><strong>Ultrasonic Sensor HC-SR04</strong>:
          <ul>
            <li>VCC → 5V</li>
            <li>TRIG → Pin 9</li>
            <li>ECHO → Pin 10</li>
            <li>GND → GND</li>
          </ul>
        </li>

        <li><strong>Servo Motor</strong>:
          <ul>
            <li>Red Wire (VCC) → 5V</li>
            <li>Brown Wire (GND) → GND</li>
            <li>Orange Wire (Signal) → Pin 6</li>
          </ul>
        </li>
      </ul>
    </section>

    <!-- How It Works -->
    <section id="how-it-works">
      <h2 class="section-title">How It Works</h2>

      <h3>System Flow</h3>
      <ol>
        <li><strong>Face Detection</strong>: Python script captures video from webcam and detects faces</li>
        <li><strong>Face Recognition</strong>: Detected face is compared with known faces database</li>
        <li><strong>Authentication</strong>: If face matches, Python sends <span class="inline-code">FACE_RECOGNIZED</span> signal to Arduino</li>
        <li><strong>Hand Detection</strong>: Arduino monitors ultrasonic sensor for hand placement</li>
        <li><strong>Dispensing</strong>: When hand is detected within range (15cm), servo motor rotates 180°</li>
        <li><strong>Reset</strong>: Servo returns to original position, Arduino signals completion</li>
        <li><strong>Loop</strong>: System returns to face detection mode for next customer</li>
      </ol>

      <h3 style="margin-top:12px;">Communication Protocol</h3>
      <div class="code-block">
<pre><code>Python → Arduino: "FACE_RECOGNIZED"
Arduino → Python: "ACK_FACE"
Arduino → Python: "HAND_DETECTED"
Arduino → Python: "DISPENSE_COMPLETE"</code></pre>
      </div>
    </section>

    <!-- Usage -->
    <section id="usage">
      <h2 class="section-title">Usage</h2>

      <h3>Running the System</h3>
      <ol>
        <li><strong>Connect Hardware</strong>: Ensure all components are connected as per circuit diagram</li>
        <li><strong>Start Arduino</strong>: Upload and run the Arduino code first</li>
        <li><strong>Run Python Script</strong>:
          <div class="code-block">
<pre><code>python face_recognition_vending.py</code></pre>
          </div>
        </li>
        <li><strong>Operation</strong>:
          <ul>
            <li>Stand in front of the camera</li>
            <li>Wait for face recognition confirmation</li>
            <li>Place hand near the dispenser (within 15cm)</li>
            <li>Item will be dispensed automatically</li>
            <li>System resets for next user</li>
          </ul>
        </li>
      </ol>

      <h3 style="margin-top:12px;">Configuration Options</h3>
      <p><strong>Arduino (<span class="inline-code">arduino_vending_machine.ino</span>)</strong>:</p>
      <div class="code-block">
<pre><code>#define DETECTION_DISTANCE 15  // Hand detection range (cm)
#define SERVO_DISPENSE_ANGLE 180  // Dispense angle
#define DISPENSE_DELAY 2000  // Hold time (ms)</code></pre>
      </div>

      <p style="margin-top:12px;"><strong>Python (adjust in your script)</strong>:</p>
      <ul>
        <li>Camera index</li>
        <li>Face recognition tolerance</li>
        <li>Serial port and baud rate</li>
      </ul>
    </section>

    <!-- Known Issues & Tips -->
    <section id="known-issues">
      <h2 class="section-title">Known Issues</h2>
      <ul>
        <li>Ensure proper lighting for face recognition</li>
        <li>Servo motor may need external power supply for heavy loads</li>
        <li>Serial communication may need adjustment based on system latency</li>
      </ul>

      <h3 style="margin-top:12px;">Tips</h3>
      <ul>
        <li>Use a good quality webcam for better face recognition</li>
        <li>Ensure stable power supply to prevent servo jitter</li>
        <li>Calibrate ultrasonic sensor distance based on your setup</li>
        <li>Keep known_faces database updated and organized</li>
      </ul>
    </section>

    <!-- Project Structure (placeholder) -->
    <section id="project-structure">
      <h2 class="section-title">Project Structure</h2>
      <p class="note">Example structure (adjust to your repo):</p>
      <div class="code-block">
<pre><code>face-recognition-vending-machine/
├─ arduino_vending_machine.ino
├─ face_recognition_vending.py
├─ known_faces/
│  ├─ alice.jpg
│  └─ bob.jpg
├─ README.md
└─ docs/</code></pre>
      </div>
    </section>

    <!-- Future Enhancements -->
    <section id="future-enhancements">
      <h2 class="section-title">Future Enhancements</h2>
      <ul>
        <li>Integrate secure user profiles and logging (who took what and when)</li>
        <li>Use a small database (SQLite) to map users to inventory limits</li>
        <li>Add payment integration (card / mobile wallet) tied to face ID</li>
        <li>Improve recognition robustness with CNN-based models or edge TPUs</li>
        <li>Provide a web dashboard for real-time monitoring and remote control</li>
      </ul>
    </section>

    <!-- Contributing -->
    <section id="contributing">
      <h2 class="section-title">Contributing</h2>
      <p>If you'd like to contribute, please fork the repository, create a feature branch, and raise a pull request. Add clear descriptions of changes and include any test instructions.</p>
    </section>

    <!-- License -->
    <section id="license">
      <h2 class="section-title">License</h2>
      <p>Specify your license here (e.g., MIT). Example:</p>
      <div class="code-block">
<pre><code>MIT License

Copyright (c) YEAR Your Name

Permission is hereby granted...</code></pre>
      </div>
    </section>

    <footer>
      <div class="note">Made with ♥ — Face Recognition Based Vending Machine • Keep your hardware safe and user data private.</div>
    </footer>
  </div>
</body>
</html>
