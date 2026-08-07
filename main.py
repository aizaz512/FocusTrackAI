from numpy import eye
import streamlit as st 
from torch import eyeeamlit as st
import cv2
from src.head_pose import HeadPoseEstimator
from src.phone_detector import PhoneDetector

from src.camera import Camera
from src.face_mesh import FaceMeshDetector
from src.eye_tracker import EyeTracker
from src.focus_analyzer import FocusAnalyzer


def main():

    camera = Camera()

    mesh = FaceMeshDetector()

    head = HeadPoseEstimator()

    phone = PhoneDetector()
    
    eye = EyeTracker()

    focus = FocusAnalyzer()

    while True:

        success, frame = camera.read_frame()

        if not success:
            break

        frame, landmarks = mesh.detect(frame)

        if landmarks:

    # Estimate head pose
            frame, direction = head.estimate(frame, landmarks)

    # Detect eye blink FIRST
            frame, closed_frames = eye.detect_blink(frame, landmarks)

    # Detect phone
            frame, phone_detected = phone.detect(frame)

    # Analyze focus
            frame = focus.analyze(
                 frame,
                closed_frames,
                phone_detected
            )
            st.session_state["focus"] = focus.focus_score
            st.session_state["status"] = focus.status
            st.session_state["blinks"] = eye.blink_counter

            history = st.session_state.get("history", [])
            history.append(focus.focus_score)
            st.session_state["history"] = history[-100:]

        cv2.imshow("FocusTrack AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    

if __name__ == "__main__":
    main()