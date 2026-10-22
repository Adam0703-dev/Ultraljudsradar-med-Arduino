# Ultraljudsradar med Arduino

## Overview

This project documents the development of an Arduino-based ultrasonic scanner with a radar-style display. A servo sweeps an ultrasonic distance sensor through 180 degrees, while a Python application displays the scan direction and detected objects.

The Arduino handles servo control and distance measurements. The desktop application receives measurements over USB serial and draws a green semicircular display using Pygame.

The project is organised around one current implementation, with firmware, desktop software, hardware notes, documentation, and test records.

## Project Structure

| Directory | Contents |
| --- | --- |
| [Firmware](./firmware/) | Arduino sketch for scanning and distance measurements. |
| [Software](./software/) | Python serial input and radar display. |
| [Hardware](./hardware/) | Components and signal connections derived from the sketch. |
| [Documentation](./docs/) | System behaviour and serial data format. |
| [Testing](./tests/) | Manual test cases and a test log template. |

## Current Implementation

- Servo sweep from 0 to 180 degrees and back.
- Distance measurement at every 6 degrees.
- Serial communication at 9600 baud.
- Radar display covering distances greater than 3 cm and up to 200 cm.
- A detected point remains visible for approximately 1.2 seconds.

The display currently shows at most one detected point at a time. Further detections are accepted after the existing point expires.

## Getting Started

1. Connect the hardware using the [hardware notes](./hardware/).
2. Open `firmware/Ultrasound_Radar/Ultrasound_Radar.ino` in Arduino IDE, select the connected board and port, and install the Servo library if required.
3. Upload the sketch and close Serial Monitor so the Python application can use the port.
4. Install the Python dependencies from the repository root:

   ```sh
   python -m pip install -r software/requirements.txt
   ```

5. Set `PORT` in `software/radar/main.py` to the Arduino's serial port. The supplied setting is `COM3`.
6. Start the display:

   ```sh
   python software/radar/main.py
   ```

The exact Arduino board, ultrasonic sensor model, and servo model are not specified in the supplied files. Select the actual board in Arduino IDE and verify electrical compatibility before connecting the hardware.

## Future Development

Possible improvements include displaying multiple detections, adding port selection, improving serial error handling, and documenting measurement accuracy through physical tests.

## Author

Developed by Adam Odeh as an electronics and programming project, with the goal of exploring ultrasonic distance measurement, servo control, and graphical visualisation.
