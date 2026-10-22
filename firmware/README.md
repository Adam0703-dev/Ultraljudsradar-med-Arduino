# Firmware

## Overview

This directory contains the Arduino firmware for the ultrasonic scanner.

Open [`Ultrasound_Radar/Ultrasound_Radar.ino`](./Ultrasound_Radar/Ultrasound_Radar.ino) in Arduino IDE. The sketch folder and file have matching names so the sketch can be opened directly.

## Dependencies

- Arduino core for the connected board.
- Servo library (`Servo.h`).

The supplied project metadata did not specify a board, so no board configuration is assumed here.

## Operation

The servo moves in one-degree increments with a 20 ms delay after each command. Measurements are transmitted at angles divisible by 6, including both sweep endpoints. The endpoints are measured again when the sweep reverses.

The ultrasonic measurement uses `pulseIn(Echo, HIGH, 15000)` and converts echo duration to centimetres using `duration * 0.0343 / 2`. A missing echo returns zero, which the display excludes from detected points. Measurement time adds to the servo delays, so the sweep duration is not fixed.

## Upload

1. Connect the Arduino by USB.
2. Select the actual board and serial port in Arduino IDE.
3. Install the Servo library if it is unavailable.
4. Verify and upload the sketch.
5. Check serial output at 9600 baud, then close Serial Monitor before starting Python.

The original sketch included an unused, empty `arduino_secrets.h` stored in a separate subdirectory. That include has been removed; the scan logic is unchanged.

See [Hardware Notes](../hardware/) for pins and [System Documentation](../docs/) for the serial protocol.
