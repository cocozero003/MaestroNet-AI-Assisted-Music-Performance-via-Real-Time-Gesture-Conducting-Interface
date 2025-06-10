import cv2
import mediapipe as mp
import tempfile

mp_pose = mp.solutions.pose

def get_wrist_y_series(video_file, hand="RIGHT"):
    """
    Extract Y-axis positions of the specified wrist from a video input.
    Args:
        video_file: Streamlit uploaded file object.
        hand (str): "RIGHT" or "LEFT" wrist.
    Returns:
        list of float: Normalized Y positions over time.
    """
    if not video_file.type.startswith("video/"):
        raise ValueError("Unsupported file type")

    # Save to temporary file for OpenCV
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp.write(video_file.read())
    temp.flush()

    cap = cv2.VideoCapture(temp.name)
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
    wrist_y = []

    wrist_idx = (
        mp_pose.PoseLandmark.RIGHT_WRIST if hand.upper() == "RIGHT"
        else mp_pose.PoseLandmark.LEFT_WRIST
    )

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.resize(frame, (640, 480))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)
        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark[wrist_idx]
            wrist_y.append(lm.y)
    cap.release()
    pose.close()
    return wrist_y
