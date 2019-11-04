void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}
char received;
int t = 700,done=0;
void loop()
{


    digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, HIGH);    // turn the LED off by making the voltage LOW
    delay(t);                       // wait for a second
  
    t=t-10;
 
  
  Serial.println(t);
  
  
  
//  if (Serial.available() > 0)
//   { received = Serial.read();
//    done=1;}
//  
//  if (done==1)
//  {
//  if (received == 'A')
//  { digitalWrite(LED_BUILTIN, HIGH);
//    delay(500);
//  }
//  if (received == 'B')
//  { digitalWrite(LED_BUILTIN, LOW);
//    delay(500);
//  }done=0;
//  }
  
}
