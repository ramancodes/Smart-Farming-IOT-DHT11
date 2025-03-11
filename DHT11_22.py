import time

def getSensorData(ser):
    try:
        # Maximum number of attempts to read data
        max_attempts = 10
        attempts = 0
        
        while attempts < max_attempts:
            attempts += 1
            
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                
                # Debug line to see what's being received
                # print(f"Raw data: {line}")  
                
                if line.startswith("T:"):
                    try:
                        parts = line.split(" H:")
                        temp = float(parts[0].replace("T:", ""))
                        hum = float(parts[1])
                        
                        data = {
                            "temperature": temp,
                            "humidity": hum
                        }
                        # print(f"Temperature: {data['temperature']}°C, Humidity: {data['humidity']}%")
                        
                        return 200, data
                    
                    except Exception as e:
                        return 400, f"Error parsing data: {e}"
            
            # Wait a bit before checking again
            time.sleep(0.5)
        
        # If we've reached the maximum attempts without data
        return 408, "Timeout waiting for sensor data"
        
    except Exception as e:
        return 500, f"Error reading sensor: {e}"