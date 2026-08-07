import cv2
import numpy as np


class HeadPoseEstimator:

    def __init__(self):
        self.direction = "Center"

    def estimate(self, frame, landmarks):

        h, w, _ = frame.shape

        face_2d = []
        face_3d = []

        # Important landmarks
        points = [33, 263, 1, 61, 291, 199]

        for idx in points:

            lm = landmarks.landmark[idx]

            x = int(lm.x * w)
            y = int(lm.y * h)

            face_2d.append([x, y])
            face_3d.append([x, y, lm.z])

        face_2d = np.array(face_2d, dtype=np.float64)
        face_3d = np.array(face_3d, dtype=np.float64)

        focal_length = w

        cam_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ])

        dist_matrix = np.zeros((4,1), dtype=np.float64)

        success, rot_vec, trans_vec = cv2.solvePnP(
            face_3d,
            face_2d,
            cam_matrix,
            dist_matrix
        )

        rmat, _ = cv2.Rodrigues(rot_vec)

        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

        x = angles[0] * 360
        y = angles[1] * 360

        if y < -10:
            self.direction = "Looking Left"

        elif y > 10:
            self.direction = "Looking Right"

        elif x < -10:
            self.direction = "Looking Down"

        elif x > 10:
            self.direction = "Looking Up"

        else:
            self.direction = "Looking Center"

        cv2.putText(
            frame,
            self.direction,
            (20,200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,0),
            2
        )

        return frame, self.direction