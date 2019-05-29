const int RDIR=22;
const int RENA=23;
const int MODE=26;
const int RCLK=5;

void setup(){
  TCCR3B = TCCR3B & B11111000 | B00000100;
  pinMode(RDIR, OUTPUT);
  digitalWrite(RDIR, HIGH);
  pinMode(RENA, OUTPUT);
  digitalWrite(RENA, HIGH);
  pinMode(MODE, OUTPUT);
  digitalWrite(MODE, HIGH);
}

void loop(){
  analogWrite(RCLK, 127);
  delay(1000);
  analogWrite(RCLK, 0);
  delay(1000);
}
