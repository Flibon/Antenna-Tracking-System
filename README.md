# Antenna-Tracking-System

This project aims to develop a system for tracking and adjusting the position of an antenna in real-time. The system will use image processing techniques to detect the position of the antenna and control motors to adjust its position as needed.

Requirements
Python 3.x
OpenCV
PySerial
Raspberry Pi (or equivalent microcontroller)
Stepper Motors and motor controllers for antenna adjustment

Getting Started
To run this project, you will need to set up your environment with the required packages. You can install the required packages by running the following command:

Copy code
pip install opencv-python numpy pyserial
Next, you will need to connect your Raspberry Pi (or equivalent microcontroller) to the camera and motors, and configure the serial connection to communicate with the motor controllers.

Running the System
To run the system, you will need to execute the main script. The script will use the gps location to determine the position of the antenna. Based on the position, the script will adjust the position of the motors to keep the antenna pointing in the desired direction.

Contributing
If you would like to contribute to this project, please feel free to fork the repository and make pull requests with your changes. We welcome contributions from all contributors, and are always looking for ways to improve the system.
