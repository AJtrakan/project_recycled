#include <Adafruit_NeoPixel.h>
#include <Servo.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(12, 13); // RX, TX

#ifdef __AVR__
#include <avr/power.h>
#endif

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;

#define neoPIN1 3
#define neoPIN2 5

#define servo1 6
#define servo2 9
#define servo3 10
#define servo4 11



#define NUMPIXELS1 2
Adafruit_NeoPixel pixels1(NUMPIXELS1, neoPIN1, NEO_GRB + NEO_KHZ800);

#define NUMPIXELS2 8
Adafruit_NeoPixel pixels2(NUMPIXELS2, neoPIN2, NEO_GRB + NEO_KHZ800);

int pos = 0;
char AA;

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);

  pixels1.begin();
  pixels2.begin();

  myservo1.attach(servo1);
  myservo2.attach(servo2);
  myservo3.attach(servo3);
  myservo4.attach(servo4);


  pixels1.setPixelColor(0, pixels1.Color(250, 250, 250));
  pixels1.setPixelColor(1, pixels1.Color(250, 250, 250));
  pixels1.show();


  for (int i = 0; i < NUMPIXELS2; i++) {
    pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
    pixels2.show();
    delay(1);
  }
  myservo1.write(180);
  myservo2.write(0);
  myservo3.write(0);
  myservo4.write(180);
  myservo1.detach();
  myservo2.detach();
  myservo3.detach();
  myservo4.detach();

}

void loop() {

  if (mySerial.available()) {
    AA = mySerial.read();
    Serial.println(AA);
  } else {
    AA = 'Z';
  }

  ////////////////////////////////////////////////////////เก็บขวด
  if (AA == 'A') {
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 250));
      pixels2.show();
      Serial.println("Neo SHOW G1");
      delay(1);
    }
    myservo1.attach(servo1);
    myservo2.attach(servo2);
    delay(1000);
    myservo1.write(0);
    myservo2.write(180);
    delay(1000);
    myservo1.write(180);
    myservo2.write(0);
    delay(1000);
    myservo1.detach();
    myservo2.detach();
    Serial.println("AAAA1");
    AA = 'Z';
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
      pixels2.show();
      Serial.println("Neo SHOW G0");
      delay(1);
    }
  } else if (AA == 'B') {                                  /////////////คืนขวด

    /////////////////////////////////////////////////////////////////
    for (int x = 0; x < 10; x++) {
      for (int i = 0; i < NUMPIXELS2; i++) {
        pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
        pixels2.show();
        Serial.println("Neo SHOW R1");
        delay(1);
      }
      delay(50);
      for (int i = 0; i < NUMPIXELS2; i++) {
        pixels2.setPixelColor(i, pixels2.Color(250, 0, 0));
        pixels2.show();
        Serial.println("Neo SHOW R1");
        delay(1);
      }
      delay(50);
    }

    /////////////////////////////////////////////////////////////////
    myservo3.attach(servo3);
    myservo4.attach(servo4);
    myservo3.write(180);
    myservo4.write(0);
    delay(1000);
    myservo3.write(0);
    myservo4.write(180);
    delay(1000);
    myservo3.detach();
    myservo4.detach();
    Serial.println("BBBB1");
    AA = 'Z';
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
      pixels2.show();
      Serial.println("Neo SHOW R0");
      delay(1);
    }
  }

  Serial.println(AA);


}
