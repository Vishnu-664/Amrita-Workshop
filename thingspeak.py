import serial
import requests
import time

# Arduino serial port, update it based on your setup
arduino_port = 'COM3'  # Change this to your Arduino's port
baud_rate = 9600

# ThingSpeak API key and channel ID
api_key = 'YOUR_THINGSPEAK_API_KEY'
channel_id = 'YOUR_THINGSPEAK_CHANNEL_ID'

# Function to read temperature from Arduino via serial
def read_temperature(serial_port):
    try:
        # Read data from Arduino
        data = serial_port.readline().decode('utf-8').strip()
        temperature = float(data)
        return temperature
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None

# Function to upload data to ThingSpeak
def upload_to_thingspeak(api_key, channel_id, temperature):
    try:
        url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={temperature}'
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Data uploaded to ThingSpeak: {temperature}")
        else:
            print(f"Failed to upload data to ThingSpeak. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error uploading data to ThingSpeak: {e}")

# Main program
if __name__ == "__main__":
    try:
        # Open serial connection to Arduino
        arduino_serial = serial.Serial(arduino_port, baud_rate, timeout=1)

        while True:
            # Read temperature from Arduino
            temperature = read_temperature(arduino_serial)

            if temperature is not None:
                # Upload data to ThingSpeak
                upload_to_thingspeak(api_key, channel_id, temperature)

            # Delay for a while before the next reading
            time.sleep(15)

    except KeyboardInterrupt:
        # Close the serial connection when the program is interrupted
        arduino_serial.close()
        print("Serial connection closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
