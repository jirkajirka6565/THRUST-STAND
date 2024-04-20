#include "HX711.h"

#define DOUT  2
#define CLK  3

HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
}

void loop() {
  // You can adjust the calibration factor to match your setup
  scale.set_scale();
  
  // Get the calibrated reading from the load cell
  float weight = scale.get_units();
  
  // Print the weight value followed by a newline character
  Serial.println(weight, 2);
  
  delay(1000);
}