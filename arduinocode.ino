const int DIR1=22;
const int ENA1=23;
const int DIR2=24;
const int ENA2=25;
const int DIR3=26;
const int ENA3=27;
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

void makemove(int st){
  if(st>0) digitalWrite(DIR1, HIGH);
  else digitalWrite(DIR1, LOW), st=-st;
  while(st){
    digitalWrite(CLK1, HIGH);
    delay(2);
    digitalWrite(CLK1, LOW);
    delay(2);
    st--;
  }
}

void push(){
  digitalWrite(DIR2, HIGH);
  st=500;       // test하고 결정
  while(st){
    digitalWrite(CLK2, HIGH);
    delay(2);
    digitalWrite(CLK2, LOW);
    delay(2);
    st--;
  }
}

void pop(){
  digitalWrite(DIR2, LOW);
  st=500;       // test하고 결정
  while(st){
    digitalWrite(CLK2, HIGH);
    delay(2);
    digitalWrite(CLK2, LOW);
    delay(2);
    st--;
  }
}
void loop(){
  if(Serial.available()){
    char com=Serial.read();
    if(com=='m'){
      int st=0;
      char a;
      while(true){
        a=Serial.read();
        if(a=='a') break;
        st=(st*10)+a-'0';
      }
      makemove(st-pos);
      pos=st;
    }
    if(com=='o'){
      int st=0;
      char a;
      while(true){
        a=Serial.read();
        if(a=='a') break;
        st=(st*10)+a-'0';
      }
      
    }
  }
}

