// Arduino code for sending temperature data over serial

const int analogPin = A0; // Analog pin for temperature sensor
const int baudRate = 9600; // Serial communication baud rate

void setup() {
  
}

void loop() {
  // Read the temperature from the sensor
  int sensorValue = analogRead(analogPin);

  // Convert the analog reading to voltage
  float voltage = sensorValue * (5.0 / 1023.0);

  // Convert the voltage to temperature in degrees Celsius
  float temperatureC = (voltage - 0.5) * 100.0;

  // Print the temperature to the serial port
  Serial.println(temperatureC);

  // Delay for a while before the next reading
  delay(1000);
}