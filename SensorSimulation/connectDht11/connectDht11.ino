#include <DHT.h>

#define DHTPIN 2     // Pin where DHT11 is connected
#define DHTTYPE DHT11  // Define sensor type

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("DHT11 test");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Format data exactly as expected by Python
  Serial.print("T:");
  Serial.print(temperature);
  Serial.print(" H:");
  Serial.println(humidity);

  delay(2000);  // Delay for 2 seconds
}