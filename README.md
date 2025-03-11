# Smart Farming IOT Sensor Microservice

## Proteus Connection
Create a proteus simulation sheet, and add the following components:
1. Arduino UNO
2. DHT11
3. COMPIM

![alt text](image.png)

## Virtual Serial Port Driver
Create a pair between COM4 and COM5, and create a virtual connection

![alt text](image-1.png)

## RUN Application
Open the terminal as administrator, nativate to the project directory, and run the following command:

```
python app.py
```

## API 

#### Get Sensor Data
Resquest:
```
http://localhost:8081/get-sensor-data
```
#### Get Sensor Data
Response [Sample]:
```
{
    "data": {
        "humidity": 90.0,
        "temperature": 27.0
    },
    "success": true
}
```