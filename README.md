# Hand Tracking with OpenCV and Mediapipe

This project captures video from a webcam and uses the MediaPipe and OpenCV libraries to detect hand landmarks and count the number of extended fingers. 

## Features
- Detects hand landmarks in real-time using the MediaPipe Hands solution.
- Counts and displays the number of extended fingers.
- Mirror-flips the image to give a more natural viewing experience.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe

## Installation

1. Clone this repository or download the code.

2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe
   ```

## Usage

1. Run the script to start the hand tracker:
   ```bash
   python hand_tracking.py
   ```

2. The program will open a webcam window displaying the hand tracker with the number of extended fingers shown at the top left corner.

3. Press `q` to quit the program.

## Code Overview

1. **Setup**:
   - Import required libraries.
   - Initialize the MediaPipe Hands model and OpenCV for video capture.

2. **Main Loop**:
   - Capture frames from the webcam.
   - Convert frames to RGB and process with MediaPipe to find hand landmarks.
   - Use the positions of landmarks to detect which fingers are extended.
   - Display the number of extended fingers on the screen.

3. **Finger Counting Logic**:
   - Thumb and other fingers are identified based on landmark positions to determine if they are extended.

## Notes
- Ensure your webcam is properly connected.
- Adjust the `fingerIds` list if using a different hand model or landmark structure.

## References
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Hands Documentation]([https://google.github.io/mediapipe/solutions/hands.html](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html))
