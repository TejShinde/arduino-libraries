const int IR1=3;
const int IR2=4;
int count =0;
int state1,state2;
void setup() {
  pinMode(IR1,INPUT);
  pinMode(IR2,OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
state1=digitalRead(IR1);
state2=digitalRead(IR2);
if (state1==1 && state2==0)
{
  while(state2==0);
  count+=1;
}

if (state1==0 && state2==1)
{
  while(state1==0);
  count-=1;
}

Serial.print("number of people inside");
Serial.println(count);

}
