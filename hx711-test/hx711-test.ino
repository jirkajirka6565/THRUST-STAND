#include "HX711.h"

#define DOUT  3
#define CLK  2
#define DOUT2 5
#define CLK2 4
#define DOUT3 7
#define CLK3 6

HX711 scale;
HX711 scale2;
HX711 scale3;

float weight;
float weight2;
float weight3;

float calFactor1;
float calFactor2;
float calFactor3;

String stringArray[10];
String InputFactor1;
String InputFactor2;
String InputFactor3;

int splitString(String data, char delimiter, String* result) {
  int index = 0;
  int startIndex = 0;
  int endIndex = 0;
  
  while ((endIndex = data.indexOf(delimiter, startIndex)) >= 0) {
    result[index++] = data.substring(startIndex, endIndex);
    startIndex = endIndex + 1;
  }
  
  // Add the last part of the string
  result[index++] = data.substring(startIndex);

  return index;  // Return the number of elements found
}

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale2.begin(DOUT2, CLK2);
  scale3.begin(DOUT3, CLK3);
  calFactor1 = 0;
  calFactor2 = 0;
  calFactor3 = 0;
}

void loop() {
  if(Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');   // Read the incoming data
    data.trim();
    Serial.println(data);
    if (data == "LC_1") {
      calFactor1 = scale.get_units();  // Set calibration for scale 1
      Serial.println("Calibrated scale 1");
    } else if (data == "LC_2") {
      calFactor2 = scale2.get_units(); // Set calibration for scale 2
      Serial.println("Calibrated scale 2");
    } else if (data == "LC_3") {
      calFactor3 = scale3.get_units(); // Set calibration for scale 3
      Serial.println("Calibrated scale 3");
    }else {
      splitString(data, "_", stringArray);
      if(stringArray[0] == "LC1"){
        InputFactor1 = stringArray[1];
      }
      else if(stringArray[0] == "LC2"){
        InputFactor2 = stringArray[1];
      }
      else if(stringArray[0] == "LC3"){
        InputFactor3 = stringArray[1];
      }
    }
  }
  // You can adjust the calibration factor to match your setup
  scale.set_scale();
  scale2.set_scale();
  scale3.set_scale();
  
  // Get the calibrated reading from the load cell
  weight = scale.get_units() - calFactor1;
  Serial.print(weight, 2);
  Serial.print(" ");

  weight2 = scale2.get_units() - calFactor2;
  Serial.print(weight2, 2);
  Serial.print(" ");

  weight3 = scale3.get_units() - calFactor3;
  Serial.println(weight3, 2);
  
  delay(500);
}