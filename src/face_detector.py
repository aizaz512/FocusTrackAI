"""
face_detector.py

Detects faces using MediaPipe Face Detection.
"""

import cv2
import mediapipe as mp


class FaceDetector:

    def __init__(self, min_detection_confidence=0.6):
        """
        Initialize the MediaPipe Face Detection model.
        """

        self.mp_face = mp.solutions.face_detection
        self.mp_draw = mp.solutions.drawing_utils

        self.face_detection = self.mp_face.FaceDetection(
            model_selection=0,
            min_detection_confidence=min_detection_confidence
        )

    def detect_faces(self, frame):
        """
        Detect faces and draw bounding boxes.
        """

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_detection.process(rgb)

        if results.detections:

            height, width, _ = frame.shape

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * width)
                y = int(bbox.ymin * height)
                w = int(bbox.width * width)
                h = int(bbox.height * height)

                confidence = detection.score[0]

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Face {confidence:.2f}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        return frame