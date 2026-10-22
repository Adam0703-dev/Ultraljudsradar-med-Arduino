# Testing

## Overview

Testing covers the serial data, servo scan, distance measurements, and Python display. Physical checks require the assembled scanner.

No physical test results were included in the supplied folder. The checks below are procedures to perform, not claims of successful operation.

## Test Cases

| ID | Check | Acceptance criteria | Status |
| --- | --- | --- | --- |
| T01 | Upload firmware | Sketch compiles for the actual board and uploads successfully. | Not tested |
| T02 | Servo sweep | Servo moves from 0 to 180 degrees and back without obstruction. | Not tested |
| T03 | Serial output | At 9600 baud, lines contain a numeric distance, semicolon, and integer angle; sampled angles are multiples of 6. | Not tested |
| T04 | Distance measurement | Record readings at known distances, calculate error, and compare against a tolerance chosen before the test. | Not tested |
| T05 | Display orientation | 0 degrees points left, 90 up, and 180 right; positions match the physical mounting. | Not tested |
| T06 | Detection lifetime | One point appears for a qualifying measurement and expires after approximately 1.2 seconds; later detections can then appear. | Not tested |
| T07 | Distance filtering | Measurements at or below 3 cm, zero readings, and measurements above 200 cm do not create detected points. | Not tested |
| T08 | Parser rejection | Wrong field counts and invalid numeric strings return no measurement without stopping the input function. | Not tested |
| T09 | Normal shutdown | Closing the window exits and releases the serial connection. | Not tested |

## Test Records

Record actual runs in [`test-log.md`](./test-log.md). Include the board, sensor, servo, power supply, software versions, and commit used so observations can be reproduced.
