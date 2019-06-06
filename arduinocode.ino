const int ENA1=22;
const int DIR1=23;
const int ENA2=24;
const int DIR2=25;
const int ENA3=26;
const int DIR3=27;
const int CLK1=5;
const int CLK2=6;
const int CLK3=7;

int pos=0;

void setup(){
  Serial.begin(9600);
  pinMode(DIR1, OUTPUT);
  pinMode(ENA1, OUTPUT);
  pinMode(DIR2, OUTPUT);
  pinMode(ENA2, OUTPUT);
  pinMode(DIR3, OUTPUT);
  pinMode(ENA3, OUTPUT);
  pinMode(CLK1, OUTPUT);
  pinMode(CLK2, OUTPUT);
  pinMode(CLK3, OUTPUT);
  digitalWrite(ENA1, HIGH);
  digitalWrite(ENA2, HIGH);
  digitalWrite(ENA3, HIGH);
}

void makemove(int a){
  int x=(a-pos)*1000;
  pos=a;
  if(x>0) digitalWrite(DIR1, LOW);
  else digitalWrite(DIR1, HIGH), x=-x;
  while(x){
    digitalWrite(CLK1, HIGH);
    delay(2);
    digitalWrite(CLK1, LOW);
    delay(2);
    x--;
  }
}

void push(){
  digitalWrite(DIR3, LOW);
  int st=3350;
  while(st){
    digitalWrite(CLK3, HIGH);
    delay(2);
    digitalWrite(CLK3, LOW);
    delay(2);
    st--;
  }
}

void pop(){
  digitalWrite(DIR3, HIGH);
  int st=3350;
  while(st){
    digitalWrite(CLK3, HIGH);
    delay(2);
    digitalWrite(CLK3, LOW);
    delay(2);
    st--;
  }
}

void opening(){
  digitalWrite(DIR2, LOW);
  for(int i=0; i<7000; i++){
    digitalWrite(CLK2, HIGH);
    delay(1);
    digitalWrite(CLK2, LOW);
    delay(1);
  }
}

void closing(int style){
  digitalWrite(DIR2, HIGH);
  int st=0;
  switch(style){
  case 4:
    st=5200;
    break;
  case 5:
    st=4300;
    break;
  case 6:
    st=3000;
    break;
  case 7:
    st=1900;
    break;
  }
  digitalWrite(DIR2, HIGH);
  for(int i=0; i<st; i++){
    digitalWrite(CLK2, HIGH);
    delay(1);
    digitalWrite(CLK2, LOW);
    delay(1);
  }
}

void loop(){
  if(Serial.available()){
    char com=Serial.read();
    if(com=='m'){
      char a;
      a=Serial.read();
      makemove(a);
    }
    if(com=='a'){
      char a;
      a=Serial.read();
      a=a-'0';
      opening();
      delay(100);
      push();
      delay(100);
      closing(a);
      delay(100);
      pop();
      delay(100);
    }
  }
}
