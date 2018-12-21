int analogPin5 = 5;     // potentiometer wiper (middle terminal) connected to analog pin 3
int analogPin4 = 4;     // potentiometer wiper (middle terminal) connected to analog pin 3
int analogPin3 = 3;     // potentiometer wiper (middle terminal) connected to analog pin 3
int analogPin2 = 2;     // potentiometer wiper (middle terminal) connected to analog pin 3
int analogPin1 = 1;     // potentiometer wiper (middle terminal) connected to analog pin 3
                        // outside leads to ground and +5V
int val5 = 0;           // variable to store the value read
int val4 = 0;           // variable to store the value read
int val3 = 0;           // variable to store the value read
int val2 = 0;           // variable to store the value read
int val1 = 0;           // variable to store the value read
int time = 0;
void setup()
{
  Serial.begin(9600);              //  setup serial
}

void loop()
{
  val1 = analogRead(analogPin1);
  val2 = analogRead(analogPin2);
  val3 = analogRead(analogPin3);
  val4 = analogRead(analogPin4);
  val5 = analogRead(analogPin5);/*
  Serial.print(val1);
  Serial.print("-");
  Serial.print(val2);
  Serial.print("-");
  Serial.print(val3);
  Serial.print("-");
  Serial.print(val4);
  Serial.print("-");
  Serial.println(val5);*/
  if (val5 >= 18) {
    Serial.println(String(15));
  }
  if (val5 <= 7) {
    Serial.println(String(05));
  }
  if (val4 >= 7) {
    Serial.println(String(14));
  }
  if (val4 <= 2) {
    Serial.println(String(04));
  }
  if (val3 >= 16) {
    Serial.println(String(13));
  }
  if (val3 <= 8) {
    Serial.println(String(03));
  }
  if (val2 >= 33) {
    Serial.println(String(12));
  }
  if (val2 <= 18) {
    Serial.println(String(02));
  }
  if (val1 >= 30) {
    Serial.println(String(11));
  }
  if (val1 <= 9) {
    Serial.println(String(01));
  }
  delay(100);
  time+=1;
  Serial.flush();
}
