import time
import random
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# MQTT client setup

root_ca_path = "your-rootCA-certificate"
private_key_path = "your-private_key"
certificate_path = "your-device_certificate"

mqttClient = AWSIoTPyMQTT.AWSIoTMQTTClient("sensorDeviceID")
mqttClient.configureEndpoint("Your Endpoint", 8883)
mqttClient.configureCredentials(root_ca_path, private_key_path, certificate_path)

mqttClient.connect()

# Define thresholds for realistic conditions
TEMPERATURE_THRESHOLD = 70  # Example threshold in degrees Celsius
SMOKE_LEVEL_THRESHOLD = 50  # Example threshold for smoke level

def generate_sensor_data():
    # Simulate normal sensor readings
    temperature = random.uniform(20, 25)  # Normal temperature range (20-25°C)
    smoke_level = random.uniform(5, 10)   # Normal smoke level (5-10 units)

    # Occasionally simulate a fire by generating values above thresholds
    if random.random() > 0.9:  # 10% chance of simulating a fire
        temperature = random.uniform(TEMPERATURE_THRESHOLD + 1, 100)  # Fire-like temperature
        smoke_level = random.uniform(SMOKE_LEVEL_THRESHOLD + 1, 100)  # Fire-like smoke level

    return {"temperature": temperature, "smoke_level": smoke_level}

while True:
    sensor_data = generate_sensor_data()
    print(f"Publishing data: {sensor_data}")
    mqttClient.publish("firesensor", json.dumps(sensor_data), 1)
    time.sleep(5)  # Send data every 5 seconds
