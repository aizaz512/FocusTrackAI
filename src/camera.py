"""
camera.py

This module is responsible for:
1. Opening the laptop camera
2. Reading video frames
3. Returning frames to the main application
"""

import cv2


class Camera:

    def __init__(self, camera_index=0):
        """
        Initialize the camera.

        camera_index = 0 means use the default laptop webcam.
        """

        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Could not open camera.")

    def read_frame(self):
        """
        Read a single frame from the webcam.

        Returns:
            success (bool)
            frame (numpy array)
        """

        success, frame = self.cap.read()

        return success, frame

    def release(self):
        """
        Release camera resources.
        """

        self.cap.release()
        cv2.destroyAllWindows()