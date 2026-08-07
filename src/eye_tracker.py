"""
eye_tracker.py

Detects blinks using Eye Aspect Ratio (EAR)
"""

import cv2
import numpy as np
from scipy.spatial import distance


class EyeTracker:

    def __init__(self):

        self.LEFT_EYE = [33,160,158,133,153,144]

        self.RIGHT_EYE = [362,385,387,263,373,380]

        self.blink_counter = 0

        self.closed_frames = 0

        self.EAR_THRESHOLD = 0.23

        self.CONSEC_FRAMES = 3


    def eye_aspect_ratio(self, eye):

        A = distance.euclidean(eye[1], eye[5])

        B = distance.euclidean(eye[2], eye[4])

        C = distance.euclidean(eye[0], eye[3])

        ear = (A + B) / (2.0 * C)

        return ear


    def detect_blink(self, frame, landmarks):

        h, w, _ = frame.shape

        left_eye = []

        right_eye = []

        for idx in self.LEFT_EYE:

            point = landmarks.landmark[idx]

            left_eye.append((int(point.x*w), int(point.y*h)))

        for idx in self.RIGHT_EYE:

            point = landmarks.landmark[idx]

            right_eye.append((int(point.x*w), int(point.y*h)))

        leftEAR = self.eye_aspect_ratio(left_eye)

        rightEAR = self.eye_aspect_ratio(right_eye)

        ear = (leftEAR + rightEAR)/2

        if ear < self.EAR_THRESHOLD:

            self.closed_frames += 1

        else:

            if self.closed_frames >= self.CONSEC_FRAMES:

                self.blink_counter += 1

            self.closed_frames = 0

        cv2.putText(
            frame,
            f"Blink Count : {self.blink_counter}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"EAR : {ear:.2f}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,0),
            2
        )

        return frame, self.closed_frames