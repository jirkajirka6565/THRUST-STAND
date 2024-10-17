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

String stringArray[1];
float InputFactor1;
float InputFactor2;
float InputFactor3;

float difference1;
float difference2;
float difference3;

void splitString(String data, char delimiter, String stringArray[], int maxParts) {
  int start = 0;
  int end = 0;
  int index = 0;

  while (index < maxParts && end != -1) {
    end = data.indexOf(delimiter, start); // Find the position of the delimiter

    if (end == -1) {
      stringArray[index] = data.substring(start); // Last part of the string
    } else {
      stringArray[index] = data.substring(start, end); // Extract the substring
    }
    
    start = end + 1; // Move past the delimiter
    index++;
  }
}

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale2.begin(DOUT2, CLK2);
  scale3.begin(DOUT3, CLK3);
  calFactor1 = 1;
  calFactor2 = 1;
  calFactor3 = 1;
  InputFactor1 = 1;
  InputFactor2 = 1;
  InputFactor3 = 1;
}

void loop() {
  if(Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');   // Read the incoming data
    data.trim();
    Serial.println("Received: " + data);
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
      splitString(data, '_', stringArray, 2);
      delay(100);
      //Serial.println(stringArray[1]);
      if(stringArray[0] == "LC1"){
        difference1 = scale.get_units() - calFactor1;
        InputFactor1 = stringArray[1].toFloat() / difference1;
        //Serial.println(stringArray[0] + " calibrating to: " + stringArray[1]);
        delay(1000);
      }
      else if(stringArray[0] == "LC2"){
        difference2 = scale2.get_units() - calFactor2;
        InputFactor2 = stringArray[1].toFloat() / difference2;
        //Serial.println(stringArray[0] + " calibrating to: " + stringArray[1]);
        delay(1000);
      }
      else if(stringArray[0] == "LC3"){
        difference3 = scale3.get_units() - calFactor3;
        InputFactor3 = stringArray[1].toFloat() / difference3;
        //Serial.println(stringArray[0] + " calibrating to: " + stringArray[1]);
        delay(1000);
      }
    }
  }
  // You can adjust the calibration factor to match your setup
  scale.set_scale();
  scale2.set_scale();
  scale3.set_scale();
  
  // Get the calibrated reading from the load cell
  weight = (scale.get_units() - calFactor1) * InputFactor1;
  Serial.print(weight, 2);
  Serial.print(" ");

  weight2 = (scale2.get_units() - calFactor2) * InputFactor2;
  Serial.print(weight2, 2);
  Serial.print(" ");

  weight3 = (scale3.get_units() - calFactor3) * InputFactor3;
  Serial.println(weight3, 2);
  
  delay(200);
}