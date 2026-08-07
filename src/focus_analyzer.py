"""
focus_analyzer.py

Analyzes user focus based on eye state.
"""

import cv2


class FocusAnalyzer:

    def __init__(self):

        self.focus_score = 100

        self.sleep_counter = 0

        self.sleep_threshold = 60      # ~2 seconds at 30 FPS

        self.status = "Focused"

    def analyze(self, frame, closed_frames, phone_detected=False):

        # Phone Detection
        if phone_detected:

            self.status = "Distracted"

            self.focus_score = max(0, self.focus_score - 2)

        elif closed_frames > self.sleep_threshold:

            self.status = "Sleeping"

            self.focus_score = max(0, self.focus_score - 1)

        else:
            
            self.status = "Focused"

            self.focus_score = min(100, self.focus_score + 1)
            

        # Sleeping Detection
        if closed_frames > self.sleep_threshold:

            self.status = "Sleeping"

            self.focus_score = max(0, self.focus_score - 1)

        else:

            self.status = "Focused"

            self.focus_score = min(100, self.focus_score + 1)

        # Status Color
        if self.status == "Focused":
            color = (0,255,0)

        elif self.status == "Sleeping":
            color = (0,0,255)

        else:
            color = (0,255,255)

        cv2.putText(
            frame,
            f"Status : {self.status}",
            (20,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

        cv2.putText(
            frame,
            f"Focus Score : {self.focus_score}%",
            (20,160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2
        )

        return frame