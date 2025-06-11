import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import uniform_filter1d

def compute_tempo_from_y_series(y_positions, fps=30):
    """
    Compute BPM from Y-axis wrist movement.
    Args:
        y_positions (list of float): Wrist Y positions.
        fps (int): Video frame rate.
    Returns:
        float: Estimated BPM.
    """
    if len(y_positions) < 5:
        return 0.0
    y = uniform_filter1d(np.array(y_positions), size=3)
    peaks, _ = find_peaks(-y, distance=fps*0.5)
    if len(peaks) < 2:
        return 0.0
    intervals = np.diff(peaks) / fps
    bpm = 60.0 / np.mean(intervals)
    return round(bpm, 2)
