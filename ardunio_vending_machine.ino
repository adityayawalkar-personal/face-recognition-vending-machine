#include <Servo.h>

#define TRIG_PIN 9        
#define ECHO_PIN 10       
#define SERVO_PIN 6       
#define DETECTION_DISTANCE 15  
#define SERVO_DISPENSE_ANGLE 180  
#define SERVO_REST_ANGLE 0        
#define DISPENSE_DELAY 2000       

Servo dispenserServo;
long duration;
int distance;
bool systemReady = false;
bool handDetected = false;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  dispenserServo.attach(SERVO_PIN);
  dispenserServo.write(SERVO_REST_ANGLE);
  delay(1000);
  Serial.println("Arduino Ready");
  Serial.println("Waiting for face recognition...");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "FACE_RECOGNIZED") {
      systemReady = true;
      Serial.println("ACK_FACE");
      Serial.println("Place hand near dispenser...");
    }
  }
  
  if (systemReady) {
    distance = measureDistance();
    if (distance > 0 && distance <= DETECTION_DISTANCE && !handDetected) {
      handDetected = true;
      Serial.println("HAND_DETECTED");
      dispenseItem();
      
      handDetected = false;
      systemReady = false;
      Serial.println("DISPENSE_COMPLETE");
      Serial.println("Ready for next customer...");
    }
    
    delay(100);
  }
}

int measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (duration == 0) {
    return -1; 
  }
  distance = duration * 0.034 / 2;
  return distance;
}

void dispenseItem() {
  Serial.println("Dispensing item...");
  dispenserServo.write(SERVO_DISPENSE_ANGLE);
  delay(DISPENSE_DELAY);
  dispenserServo.write(SERVO_REST_ANGLE);
  delay(500);
  Serial.println("Item dispensed!");
}

void emergencyStop() {
  systemReady = false;
  handDetected = false;
  dispenserServo.write(SERVO_REST_ANGLE);
  Serial.println("EMERGENCY_STOP");
}