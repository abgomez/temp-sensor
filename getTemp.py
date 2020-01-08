import time
import json
import board
import adafruit_dht
from flask import Flask

app = Flask(__name__)

sensor = {'ID': "nodeA", 'Temperature': 0.0, 'Humidity': 0.0}

@app.route("/data", methods=["GET"])
def getValues():
    try:
        # Get sensor reads
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        sensor["Temperature"] = float(temperature)
        sensor["Humidity"] = float(humidity)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        return error.args[0]
    return json.dumps(sensor)

if __name__ == '__main__':
    # Initial the dht device, with data pin connected to:
    dhtDevice = adafruit_dht.DHT11(board.D18)
    app.run(port=8080)