import numpy as np
from PantoMatrix.emage_evaltools.metric import BC

_bc = BC(download_path="third_party/PantoMatrix/emage_evaltools/")

def evaluate_beat_coherence(audio_path, wrist_y, fps=30):
    """
    Compute beat coherence score between audio and wrist motion.
    Args:
        audio_path (str): Path to reference audio (.wav).
        wrist_y (list of float): Wrist Y positions.
        fps (int): Frame rate of motion data.
    Returns:
        float: Coherence score (lower = better).
    """
    audio_beat = _bc.load_audio(audio_path, t_start=0, t_end=None, audio_fps=16000)
    motion = np.array(wrist_y).reshape(-1,1)
    motion_beat = _bc.load_motion(motion, t_start=0, t_end=None, pose_fps=fps, without_file=True)
    return _bc.compute(audio_beat, motion_beat, length=len(wrist_y), pose_fps=fps)
