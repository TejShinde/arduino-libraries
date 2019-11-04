#include <Servo.h>

Servo myservo;
int pos=180;
const int ck=3;
const int ack=4;
void setup()
{

myservo.attach(2);
pinMode(ck,INPUT);
pinMode(ack,INPUT);
Serial.begin(9600);

}

void loop()
{

  if(ck==0 && ack==1)
  {
    myservo.write(pos++);
    Serial.print("clockwise");
    Serial.print(pos);
  }
  
  else if(ck==1 && ack==0)
  {
    myservo.write(pos--);
    Serial.print("anti-clockwise");
    Serial.print(pos);
  }
  
  else if(ck==1 && ack==1)
    {
    myservo.write(pos);
    Serial.print("stopped");
    Serial.print(pos);
    }
}
