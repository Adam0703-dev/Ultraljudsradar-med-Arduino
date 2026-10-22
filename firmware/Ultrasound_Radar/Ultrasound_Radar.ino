#include <Servo.h>

Servo radarServo;

// Pin outputs and names

#define Trig 13
#define Echo 12
#define servoPin 8


void setup() {

  Serial.begin(9600);

  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
  
  radarServo.attach(servoPin);


}


void loop() {

  servoScan();

}

void servoScan() {

  for ( int vinkel = 0; vinkel <= 180; vinkel++) {

    radarServo.write(vinkel);
    delay(20);

    if (vinkel % 6 == 0){

      Serial.print(matAvstand(),1);
      Serial.print(";");
      Serial.println(vinkel);

    }

  }

  for (int vinkel = 180; vinkel >= 0; vinkel--){

    radarServo.write(vinkel);
    delay(20);
    
    if (vinkel % 6 == 0){

    Serial.print(matAvstand(),1);
    Serial.print(";");
    Serial.println(vinkel);

    }

  }
 
}


float matAvstand() {

  digitalWrite(Trig, LOW);
  delayMicroseconds(20);

  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

  unsigned long total_tid = pulseIn(Echo, HIGH, 15000);

  float distans = total_tid * 0.0343/2;

  return distans;

}