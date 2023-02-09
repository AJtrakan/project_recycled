#include <HardwareSerial.h>

HardwareSerial SeriaL1(1);
HardwareSerial SeriaL2(2);


#define RX1_pin 19
#define TX1_pin 18
#define RX2_pin 16
#define TX2_pin 17


char AA;
char AB;
int Sta = 0;

void setup() {
  Serial.begin(115200);
  SeriaL1.begin(9600, SERIAL_8N1, RX1_pin, TX1_pin);  //ไป arduino
  SeriaL2.begin(9600, SERIAL_8N1, RX2_pin, TX2_pin);  //ไป rpi

}

void loop() {

  if (Serial.available()) {
    AA = Serial.read();
    Serial.println(AA);
    SeriaL1.write(AA);
    SeriaL2.write(AA);
  }

  if (SeriaL1.available()) {
    AA = SeriaL1.read();
    Serial.print("SeriaL1 = ");
    Serial.println(AA);
    if (Sta == 0) {
      SeriaL2.write(AA);
      SeriaL1.write(AA);
      Sta = 1;
    }
    if(AA == 'N'){
      Sta = 0;
    }
  }

  if (SeriaL2.available()) {
    AB = SeriaL2.read();
    if (AB == 'O') {
      Serial.println("SeriaL2 = OK");
      SeriaL1.write('A');
      Sta = 0;
    } else if (AB == 'E') {
      Serial.println("SeriaL2 = Error");
      SeriaL1.write('B');
      Sta = 0;
    } else if (AB == 'N') {
      Serial.println("SeriaL2 = N");
      //SeriaL1.write('B');
      Sta = 0;
    } else {
      Serial.println("SeriaL2 = ");
      Serial.println(AB);
      SeriaL1.write(AB);
    }
  }

}
