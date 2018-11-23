int analogPin5 = 5;     // potentiometer wiper (middle terminal) connected to analog pin 3
                       // outside leads to ground and +5V
int val5 = 0;           // variable to store the value read
int time = 0;
void setup()
{
  Serial.begin(9600);              //  setup serial
}

void loop()
{
  val5 = analogRead(analogPin5);     // read the input pin
  if (val5 >= 9) {
    Serial.println(String(1));
  }
  if (val5 <= 5) {
    Serial.println(String(0));
  }
  delay(100);
  time+=1;
  Serial.flush();
}
