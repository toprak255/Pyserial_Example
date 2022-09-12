
int xcoord;
int ycoord;
int button;
String t=",";

void setup() {
pinMode(A3,INPUT);
pinMode(A1,INPUT);
pinMode(2,INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
  xcoord = analogRead(A3);
  ycoord = analogRead(A1);
  button = digitalRead(2);
  Serial.println(xcoord+t+ycoord+t+button);
  delay(50);


}
