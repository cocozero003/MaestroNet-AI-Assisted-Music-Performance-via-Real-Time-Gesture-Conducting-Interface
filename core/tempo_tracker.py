import numpy as np
from scipy.signal import find_peaks

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
    y = np.array(y_positions)
    # smooth to reduce jitter
    from scipy.ndimage import uniform_filter1d
    y = uniform_filter1d(y, size=3)
    inverted = -y
    peaks, _ = find_peaks(inverted, distance=fps * 0.5)
    if len(peaks) < 2:
        return 0.0
    intervals = np.diff(peaks) / fps
    avg_interval = np.mean(intervals)
    bpm = 60.0 / avg_interval
    return round(bpm, 2)
