import numpy as np

def map_dynamics_from_gesture(y_positions):
    """
    Estimate dynamic level from movement speed.
    Args:
        y_positions (list of float): Wrist Y positions.
    Returns:
        str: Dynamic level: pp, p, mp, mf, f, ff.
    """
    if len(y_positions) < 2:
        return "mf"
    diffs = np.abs(np.diff(y_positions))
    avg_speed = np.mean(diffs)
    if avg_speed < 0.005:
        return "pp"
    elif avg_speed < 0.01:
        return "p"
    elif avg_speed < 0.02:
        return "mp"
    elif avg_speed < 0.03:
        return "mf"
    elif avg_speed < 0.04:
        return "f"
    else:
        return "ff"
