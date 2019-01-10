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
  Serial.print(val5);
  Serial.print("-");
  Serial.print(val4);
  Serial.print("-");
  Serial.print(val3);
  Serial.print("-");
  Serial.print(val2);
  Serial.print("-");
  Serial.println(val1);*/
  if (val5 >= 5) {
    Serial.print(String(15));
  }
  if (val5 <= 4) {
    Serial.print(String(5));
  }
  if (val4 >= 4) {
    Serial.print(String(14));
  }
  if (val4 <= 2) {
    Serial.print(String(4));
  }
  if (val3 >= 16) {
    Serial.print(String(13));
  }
  if (val3 <= 8) {
    Serial.print(String(3));
  }
  if (val2 >= 7) {
    Serial.print(String(12));
  }
  if (val2 <= 4) {
    Serial.print(String(2));
  }
  if (val1 >= 30) {
    Serial.print(String(11));
  }
  if (val1 <= 9) {
    Serial.print(String(1));
  }
  Serial.println();
  delay(100);
  Serial.flush();
}
