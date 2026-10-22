# Hardware Notes

## Overview

The firmware controls a servo and measures distance using a trigger/echo ultrasonic sensor. The component roles and signal pins below are derived from the supplied code; no schematic or component list was supplied.

## Bill of Materials

| Component | Model / Specification | Quantity | Function |
| --- | --- | ---: | --- |
| Arduino-compatible board | Model unspecified | 1 | Controls scanning and sends measurements. |
| Ultrasonic distance sensor | Trigger/echo interface; model unspecified | 1 | Measures distance. |
| Servo | Model unspecified | 1 | Rotates the sensor. |
| USB cable | Compatible with the board | 1 | Upload and serial communication. |
| Jumper wires and mounting | As required | As required | Connections and sensor mounting. |

## Signal Connections

| Signal | Arduino pin | Sketch identifier |
| --- | --- | --- |
| Sensor trigger | D13 | `Trig` |
| Sensor echo | D12 | `Echo` |
| Servo signal | D8 | `servoPin` |

## Power and Assembly

Verify the board's logic voltage, the sensor's echo voltage, and the servo's supply requirements against the actual component specifications. Use a suitable servo power supply and a common signal ground. Power connections cannot be established from the code alone.

Mount the sensor so that the servo's commanded 0–180 degree movement is mechanically unobstructed. Check that cables can move freely through the full sweep.

## Documentation Status

The source folder contains code only. Wiring diagrams, photographs, component model numbers, and power-supply details have not yet been supplied.
