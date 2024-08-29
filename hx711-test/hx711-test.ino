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

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale2.begin(DOUT2, CLK2);
  scale3.begin(DOUT3, CLK3);
}

void loop() {
  // You can adjust the calibration factor to match your setup
  scale.set_scale();
  scale2.set_scale();
  scale3.set_scale();
  
  // Get the calibrated reading from the load cell
  float weight = scale.get_units();
  Serial.print(weight, 2);
  Serial.print(" ");

  float weight2 = scale2.get_units();
  Serial.print(weight2, 2);
  Serial.print(" ");

  float weight3 = scale3.get_units();
  Serial.println(weight3, 2);
  
  delay(500);
}