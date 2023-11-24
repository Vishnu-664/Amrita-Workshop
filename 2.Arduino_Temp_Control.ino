const int sensorPin = A0;   // Analog pin for NTC sensor
const int relayPin = 2;     // Digital pin for relay

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
}
void loop() {
  // Read temperature from NTC sensor
  int sensorValue = analogRead(sensorPin);
  float voltage = sensorValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100.0;

  // Control the relay based on temperature
  if (temperature > 25.0) {
    digitalWrite(relayPin, HIGH);  // Turn on the relay
  } else {
    digitalWrite(relayPin, LOW);   // Turn off the relay
  }

  // Send data to serial
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  delay(1000);  // Adjust delay as needed
}
