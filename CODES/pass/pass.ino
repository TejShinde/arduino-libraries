 
 

char Received = 0;
String password;

int count = 0;
int flag = 0;

 

void setup() {
  // set up the LCD's number of columns and rows:
 
 
  Serial.begin(9600);
Serial.print("welcome");
} 
int go = 0;
void loop() {
//Serial.println("welcome");
  while (Serial.available() > 0)
  {
    delay(10);
    Received = Serial.read();
    if (Received == '*' || Received == 0x0D || Received == 0x0A)
    {
      break;
    }
    password += Received;
    go = 1;
  }
  
  if (go == 1)
  {
 
    if (password == "infinity")
    {
   
     Serial.println("Correct Password");
      
    }
    else
    {
     
      Serial.println("wrong password");
      count += 1;
      flag = 1;
      password="";
    }
    go = 0;
  }
  
    if(count==5 && flag==1)
    {
       Serial.println("please try again after 5 sec");
      delay(5000);
      count=0;
      flag=0;
    }
  delay(500);
}
