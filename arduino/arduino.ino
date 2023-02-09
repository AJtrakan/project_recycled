#include <Adafruit_NeoPixel.h>
#include <Servo.h>
#include <SoftwareSerial.h>
#include "Adafruit_Thermal.h"

SoftwareSerial mySerial1(12, 13); // RX, TX
//SoftwareSerial mySerial(7, 8); // RX, TX
#include <avr/power.h>

Adafruit_Thermal printer(&Serial);

#ifdef __AVR__
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
  Serial.begin(9600);
  mySerial1.begin(9600);
  //mySerial.begin(9600);

  printer.begin();

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
  Serial.println(".....START.....");
  H_Print();
  printer.justify('C');
  printer.setSize('L');
  printer.println(F("START"));
  L_Print();

}

void loop() {


  //
  //  if (Serial.available()) {
  //    AA = Serial.read();
  //    Serial.println(AA);
  //  } else {
  //    AA = 'Z';
  //  }


  if (mySerial1.available()) {
    AA = mySerial1.read();
    // Serial.print("mySerial = ");
    // Serial.println(AA);
  } else {
    AA = 'Z';
  }

  ////////////////////////////////////////////////////////เก็บขวด
  if (AA == 'A') {
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 250));
      pixels2.show();
      //  Serial.println("Neo SHOW G1");
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
    // Serial.println("AAAA1");
    AA = 'Z';
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
      pixels2.show();
      //Serial.println("Neo SHOW G0");
      delay(1);
    }
  } else if (AA == 'B') {                                  /////////////คืนขวด

    /////////////////////////////////////////////////////////////////
    for (int x = 0; x < 10; x++) {
      for (int i = 0; i < NUMPIXELS2; i++) {
        pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
        pixels2.show();
        //Serial.println("Neo SHOW R1");
        delay(1);
      }
      delay(50);
      for (int i = 0; i < NUMPIXELS2; i++) {
        pixels2.setPixelColor(i, pixels2.Color(250, 0, 0));
        pixels2.show();
        //Serial.println("Neo SHOW R1");
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
    //Serial.println("BBBB1");
    AA = 'Z';
    for (int i = 0; i < NUMPIXELS2; i++) {
      pixels2.setPixelColor(i, pixels2.Color(0, 0, 0));
      pixels2.show();
      //Serial.println("Neo SHOW R0");
      delay(1);
    }
  }
  /////////////////////////////////////////////////////////////////

  if (AA == '1') {
    //Serial.println("1 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("1"));
    L_Print();
  }

  if (AA == '2') {
    //Serial.println("2 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("2"));
    L_Print();
  }

  if (AA == '3') {
    //Serial.println("3 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("3"));
    L_Print();
  }
  if (AA == '4') {
    //Serial.println("4 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("4"));
    L_Print();
  }

  if (AA == '5') {
    //Serial.println("5 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("5"));
    L_Print();
  }

  if (AA == '6') {
    //Serial.println("6 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("6"));
    L_Print();
  }
  if (AA == '7') {
    //Serial.println("7 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("7"));
    L_Print();
  }
  if (AA == '8') {
    //Serial.println("8 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("8"));
    L_Print();
  }
  if (AA == '8') {
    //Serial.println("9 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("9"));
    L_Print();
  }
  if (AA == '0') {
    //Serial.println("10 THB");
    H_Print();
    printer.justify('C');
    printer.setSize('L');
    printer.println(F("10"));
    L_Print();
  }

  //Serial.println(AA);
}

void H_Print() {
  printer.feed(1);
  printer.setFont('B');
  printer.println("...............................");
  printer.feed(1);
  printer.justify('C');
  printer.setSize('S');
  printer.println(F("The machine Purchase of"));
  printer.println(F("recycled plastic bottles sorted"));
  printer.println(F("by AI system"));
  printer.feed(1);

  printer.doubleHeightOn();
  printer.justify('C');
  printer.println(F("Discount Coupon"));

  printer.doubleHeightOff();
  printer.feed(1);

}

void L_Print() {
  printer.justify('R');
  printer.setSize('M');
  printer.println(F("THB"));
  printer.feed(1);
  printer.justify('C');
  printer.setSize('S');
  printer.println(F("Electronics Department"));
  printer.println(F("Lanna Poly technic ChiangMai"));
  printer.feed(1);
  printer.println("...............................");
  printer.feed(2);

}
