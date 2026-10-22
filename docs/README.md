# System Documentation

## Overview

The Arduino commands the servo angle, measures an ultrasonic echo, and sends a distance/angle pair to the desktop application. Python converts the pair to screen coordinates and redraws the radar display.

The visualisation resembles radar, while the distance measurement itself uses ultrasound.

## Serial Protocol

- Baud rate: **9600**.
- Format: **distance_cm;angle_degrees**, followed by a newline.
- Distance: one decimal place in the firmware output.
- Angle: integer from 0 to 180 in the current sweep.

Example line:

```text
42.7;90
```

This represents a measured distance of 42.7 cm at a commanded servo angle of 90 degrees. The angle is the commanded position; no position feedback is read.

## Display Coordinates

The display origin is `(400, 450)` and the scale is 2 pixels per centimetre:

```text
x = 400 - 2 × distance × cos(angle)
y = 450 - 2 × distance × sin(angle)
```

The angle is converted to radians before applying the trigonometric functions. Zero degrees points left, 90 degrees points up, and 180 degrees points right.

The scan line follows valid parsed angle measurements. A detected point is added only for `3 < distance <= 200` and only when no previous point remains visible.

## Project Organisation

The repository contains one current implementation. Development history is recorded through Git commits; no numbered version directories or releases are used.

Hardware details are in [Hardware Notes](../hardware/), setup instructions are in [Software](../software/), and physical checks are in [Testing](../tests/).
