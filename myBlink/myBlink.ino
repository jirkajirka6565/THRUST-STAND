
int x;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  
  while (!Serial.available()); 
	x = Serial.readString().toInt(); 
  if(x == 1)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Led on");
  }
  else if (x == 0)
  {
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Led off");
  }

}
