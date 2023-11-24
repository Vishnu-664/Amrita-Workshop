import serial
import time

# Replace 'YOUR_ARDUINO_PORT' with the correct port for your Arduino
arduino_port = 'YOUR_ARDUINO_PORT'
baud_rate = 9600

try:
    # Open serial connection to Arduino
    arduino_serial = serial.Serial(arduino_port, baud_rate, timeout=1)

    while True:
        # Read data from Arduino
        data = arduino_serial.readline().decode('utf-8').strip()

        # Print the received data
        print(f"Received data from Arduino: {data}")

        # Delay for a while before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    # Close the serial connection when the program is interrupted
    arduino_serial.close()
    print("Serial connection closed.")
except Exception as e:
    print(f"An error occurred: {e}")
