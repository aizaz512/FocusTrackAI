from ultralytics import YOLO
import cv2


class PhoneDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

        self.phone_detected = False

        self.phone_count = 0

    def detect(self, frame):

        self.phone_detected = False

        results = self.model(frame, verbose=False)

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                label = self.model.names[cls]

                if label == "cell phone":

                    self.phone_detected = True

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        2
                    )

                    cv2.putText(
                        frame,
                        "PHONE DETECTED",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

        if self.phone_detected:
            self.phone_count += 1

        cv2.putText(
            frame,
            f"Phone Count : {self.phone_count}",
            (20,240),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,0,255),
            2
        )

        return frame, self.phone_detected