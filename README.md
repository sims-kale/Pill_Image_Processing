# Pill Image Processing

This project involves processing images of pills to detect and count blue pills using OpenCV and Python.

### Requirements

- Python 3.x
- OpenCV
- Matplotlib

### Image Reading and Displaying
This code reads an image from the specified file path and checks if the image was loaded successfully.

### Image Processing
The script performs the following steps:

- Converts the image from BGR to RGB.
- Applies Gaussian blur to the image.
- Applies mean shift filtering to the image.
- Converts the image to a binary image using threshold values for blue color.
- Finds contours in the binary image.
