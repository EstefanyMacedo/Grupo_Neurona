int period = 5;
unsigned long lastMsg = 0;
float F = 1;
double Fs = 10*F;
double Ts_ms = (1/Fs)*1000;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while(!Serial);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long now = millis();
  if (now - lastMsg > Ts_ms){
    lastMsg - now;
    int r1 = random(10);
    int r2 = random(10);

    Serial.print("Señal1:");
    Serial.print(r1);
    Serial.print(",");
    Serial.print("Señal2:");
    Serial.print(r2);
    }
}
