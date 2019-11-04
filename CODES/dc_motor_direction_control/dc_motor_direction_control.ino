const int MotorPos=3;
const int MotorNeg=4;
const int button1=5;
const int button2=6;

int clk=0,aclk=0;
void setup() {
  // put your setup code here, to run once:
pinMode(MotorPos,OUTPUT);
pinMode(MotorNeg,OUTPUT);
pinMode(button1,INPUT);
pinMode(button2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

clk=digitalRead(button1);
aclk=digitalRead(button1);

if (clk==0 && aclk==1)
{
  digitalWrite(MotorPos,HIGH);
  digitalWrite(MotorNeg,LOW);
  
}
else if (clk==1 && aclk==0)
{
  digitalWrite(MotorPos,LOW);
  digitalWrite(MotorNeg,HIGH);
  
}
else if (clk==aclk)
{
  digitalWrite(MotorPos,HIGH);
  digitalWrite(MotorNeg,LOW);
  
}









}
