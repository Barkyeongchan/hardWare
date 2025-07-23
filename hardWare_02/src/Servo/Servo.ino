#include <Servo.h>

int button = 7;
bool lastButtonState = HIGH;
bool triggered = false;

Servo myservo;

void setup(){
  Serial.begin(9600);
  pinMode(button, INPUT_PULLUP);
  myservo.attach(6);
}

void loop(){
  int state = digitalRead(button);

  if (lastButtonState == HIGH and state == LOW){
    triggered = true;
  }
  lastButtonState = state;
  if (triggered){
    Serial.println(triggered);
    for (int i = 1; i <= 10; i++){
    myservo.write(90);
    delay(500);
    myservo.write(180);
    delay(500);
    }
    triggered = false;
    Serial.println(triggered);
  }
}
