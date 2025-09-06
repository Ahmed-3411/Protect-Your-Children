#include <Servo.h>

#define TRIG 9
#define ECHO 10
#define BUZZER 7
#define SERVO_PIN 6

Servo windowServo;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(BUZZER, OUTPUT);
  windowServo.attach(SERVO_PIN);
  windowServo.write(0);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH);
  int distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.println(distance);

  if (distance < 30) {
    digitalWrite(BUZZER, HIGH);
    windowServo.write(90);
    Serial.println("Warning: Child near window!");
    delay(1000);
  } else {
    digitalWrite(BUZZER, LOW);
    windowServo.write(0);
  }

  delay(200);
}