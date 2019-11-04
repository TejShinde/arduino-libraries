const int sensor = A0;


#include <LiquidCrystal.h> 
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int data;
float pressure;
void setup() 
{
  // put your setup code here, to run once:
  pinMode(sensor,INPUT);
  lcd.begin(16, 2);
  lcd.setCursor(0,1);
  lcd.print("pressure");
  lcd.setCursor(1,1);
}

void loop() {
  // put your main code here, to run repeatedly:
data=digitalRead(sensor);
pressure=map(data,0,1023,1,3);
lcd.print(pressure);



}
