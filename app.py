import time
from flask import Flask, request, jsonify
from DHT11_22 import getSensorData
import serial

# Global serial connection
ser = None

def initialize_serial():
    global ser
    try:
        # Trying to close any existing connection first
        if ser is not None:
            try:
                ser.close()
            except:
                pass
        
        # Configuring serial port/connecting to port COM5
        ser = serial.Serial('COM5', 9600, timeout=1)
        time.sleep(2)
        print(f"Connected to {ser.port}")
        return True
    except Exception as e:
        print(f"Error initializing serial: {e}")
        return False

def getData():
    global ser
    # Make sure we have a valid serial connection
    if ser is None or not ser.is_open:
        if not initialize_serial():
            return 500, {"error": "Could not initialize serial connection"}
    
    # Get sensor data
    status, data = getSensorData(ser)
    # print(f"Status: {status}, Data: {data}")
    return status, data

app = Flask(__name__)

@app.route('/check', methods=["GET"])
def check_api():
    return "API is working", 200

@app.route('/get-sensor-data', methods=["GET"])
def get_sensor_data():
    try:
        status, data = getData()
        if status == 200:
            return jsonify({"success": True, "data": data}), 200
        else:
            return jsonify({"success": False, "error": f"Failed to get sensor data {data}"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    # Initialize the serial connection before starting the Flask app
    initialize_serial()
    
    # Get initial data to verify connection
    try:
        getData()
    except Exception as e:
        print(f"Initial data fetch failed: {e}")
    
    try:
        app.run(debug=False, port=8081, use_reloader=False)
    finally:
        # Close the serial connection when the app exits
        if ser is not None and ser.is_open:
            ser.close()
            print("Serial connection closed")