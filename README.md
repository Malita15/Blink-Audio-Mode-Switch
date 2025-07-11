## Quick Explanation of how it works :
Project Title:
Audio Mode Activation via Blink Detection

Objective:
To create a system that activates voice command mode using a triple blink gesture, allowing the user to perform system tasks hands-free through voice commands.

list of Software Requirements:

Python 3.x

OpenCV

Dlib

Scipy

SpeechRecognition

Pyttsx3

PyWhatKit

Webbrowser

Subprocess


Working Principle:

The system uses OpenCV and Dlib to capture live video and detect a triple blink gesture.

On detecting the triple blink, it activates Audio Mode.

In Audio Mode, using SpeechRecognition, the system listens for specific voice commands and executes tasks:

Saying "I want to do shopping" opens Amazon.

Saying "Open Chrome" launches the Google Chrome browser.

Saying "Play [song]" plays the song on YouTube using PyWhatKit.

Saying "Stop" deactivates Audio Mode.


Pyttsx3 is used for text-to-speech feedback, enhancing interactivity.


Conclusion:
This project demonstrates a practical, accessible solution for hands-free system control using blink detection and voice commands. It combines computer vision and speech recognition modules effectively.



-------------------------------------------------


## Brief Description :

**Blink Audio Mode Switch** is an intelligent system that allows users to switch between gesture and audio control modes by detecting a **triple blink**. It leverages facial landmark detection to activate voice command navigation and provides audio feedback to the user. The goal is to enable hands-free interaction using simple eye gestures and voice commands.

## Features of this project :

- **Triple Blink Detection**: Detects a triple blink to seamlessly switch from gesture mode to audio control mode.
- **Audio Mode Activation**: Activates audio mode upon detecting a triple blink, enabling voice commands for system navigation.
- **Voice Command Recognition**: Uses speech recognition to process user commands in audio mode, allowing voice-driven interactions.
- **Real-time Audio Feedback**: Provides immediate audio feedback to inform the user of actions and system status.
- **Offline Operation**: The system is designed to function offline, making it suitable for environments with limited internet access.

## Installation :

### Prerequisites :

- Python 3.x
- Required libraries listed in `requirements.txt`.

### Steps

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/Blink_Audio_Mode_Switch.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Blink_Audio_Mode_Switch
   ```

3. Install the necessary Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that the model files (such as `shape_predictor_68_face_landmarks.dat`) are placed in the project directory.

## Usage

1. Run the main script to start the system:

   ```bash
   python main.py
   ```

2. The system will detect a triple blink and activate the audio mode.
3. Once in audio mode, you can issue voice commands to control the system or trigger specific actions.
4. The system will provide audio feedback to inform the user of its actions.

## Contributing

We welcome contributions to enhance the functionality and performance of the system. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Added feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



