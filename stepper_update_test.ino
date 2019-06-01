const int RDIR=22;
const int RENA=23;
const int MODE=26;
const int RCLK=5;
int STEP=20;
int TURN=1;

void setup(){
  Serial.begin(9600);
  pinMode(RDIR, OUTPUT);
  digitalWrite(RDIR, HIGH);
  pinMode(RENA, OUTPUT);
  digitalWrite(RENA, HIGH);
  pinMode(MODE, OUTPUT);
  digitalWrite(MODE, HIGH);
  pinMode(RCLK, OUTPUT);
}

void loop(){
  digitalWrite(RCLK, HIGH);
  delay(3);
  digitalWrite(RCLK, LOW);
  delay(4);
  STEP--;
  if(STEP==0){
    STEP=20;
    delay(1000);
  }
}
