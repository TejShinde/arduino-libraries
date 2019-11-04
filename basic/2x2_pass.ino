 
const int k1=3;
const int k2=4;
const int k3=5;
const int k4=6;
String password;
int v1,v2,v3,v4;
void setup() 
{ 
pinMode(k1,INPUT);
pinMode(k2,INPUT);
pinMode(k3,INPUT);
pinMode(k4,INPUT);


}
int done=0,count=0;
void loop() 
{
if (done==0)
{ Serial.println("enter password");
  if (digitalRead(k1)==0)
  password+='A';
  else if(digitalRead(k2)==0)
  password+='B';
    else if(digitalRead(k3)==0)
  password+='C';
    else if(digitalRead(k4)==0)
  password+='D';
  count++;
  if (count==4)
  done=1;
}

if (done==1)
{
  if (password=="ADBC")
  {
    Serial.println("correct password");
  }
  else
  {
    Serial.println("wrong password");
  }
  done=0;
}


}
