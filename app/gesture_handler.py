from core.pose_estimation import get_wrist_y_series
from core.tempo_tracker import compute_tempo_from_y_series
from core.dynamics_mapper import map_dynamics_from_gesture

def process_video_for_bpm(video_file, fps=30):
    """
    Process uploaded video to estimate BPM and dynamic level.
    Returns:
        tuple: (bpm, dynamic_level)
    """
    y_series = get_wrist_y_series(video_file)
    bpm = compute_tempo_from_y_series(y_series, fps=fps)
    dynamic = map_dynamics_from_gesture(y_series)
    return bpm, dynamic
