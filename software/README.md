# Radar Software

## Overview

The Python application reads the Arduino's serial output and displays measurements in an 800 × 600 Pygame window.

| File | Purpose |
| --- | --- |
| [`radar/main.py`](./radar/main.py) | Serial connection, event loop, and detection lifetime. |
| [`radar/Radar_Input.py`](./radar/Radar_Input.py) | Parses distance and angle from each serial line. |
| [`radar/Radar_Grafik.py`](./radar/Radar_Grafik.py) | Draws the grid, scan line, and detected point. |

## Installation and Use

Install Python and run the following commands from the repository root:

```sh
python -m pip install -r software/requirements.txt
python software/radar/main.py
```

Set `PORT` in `radar/main.py` to the connected device before starting. Close other programs using the same port. The original Python source files are retained unchanged.

## Configuration

| Setting | Default | Meaning |
| --- | --- | --- |
| `PORT` | `COM3` | Arduino serial port. |
| `BAUD` | `9600` | Must match the firmware. |
| `FPS` | `60` | Target display frame rate. |
| `KVARTID_MS` | `1200` | Detection lifetime in milliseconds. |
| `MAX_DISTANS` | `200` | Maximum displayed distance in centimetres. |

The graphics use a fixed scale of 2 pixels per centimetre. Changing `MAX_DISTANS` alone does not resize the grid.

## Current Limitations

- Only one point is stored at a time; subsequent detections are ignored until it expires.
- Lines with the wrong number of fields or invalid numeric values are rejected. Numeric ranges and non-finite values are not validated.
- A partial serial line can block reading for up to the one-second serial timeout.
- Serial connection failures are not presented in a graphical error dialog.
- Python and dependency versions have not been pinned to a verified configuration.

Close the radar window to exit. The serial port and Pygame resources are then released.
