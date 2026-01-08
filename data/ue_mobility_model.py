"""
Gauss-Markov Mobility Model for User Equipment (UE) Simulation
This implementation provides functions to initialize and update the state of UEs based on the Gauss-Markov model.
Alpha is kept reasonably close to 1 to ensure smooth mobility patterns.
"""
import numpy as np

ALPHA = 0.85
MEAN_SPEED = 1.5
STD_SPEED = 0.5
DELTA_T = 1
AREA_SIZE = 1000

def initialize_ue():
    """Initialize UE with random position, speed, and direction."""
    return {
        "x": np.random.uniform(0, AREA_SIZE),
        "y": np.random.uniform(0, AREA_SIZE),
        "speed": np.random.normal(MEAN_SPEED, STD_SPEED),
        "direction": np.random.uniform(0, 2*np.pi)
    }

def update_ue_state(state):
    """Update UE state based on the Gauss-Markov mobility model.
    Parameters:
    state (dict): Current state of the UE with keys 'x', 'y', 'speed', 'direction'.
    Returns:
    dict: Updated state of the UE."""
    speed = ALPHA * state["speed"] + (1 - ALPHA) * np.random.normal(MEAN_SPEED, STD_SPEED)
    direction = ALPHA * state["direction"] + (1 - ALPHA) * np.random.uniform(0, 2*np.pi)

    x = state["x"] + speed * np.cos(direction) * DELTA_T
    y = state["y"] + speed * np.sin(direction) * DELTA_T

    """Ensure UEs stay within the area restricted by AREA_SIZE."""
    x = max(0, min(AREA_SIZE, x))
    y = max(0, min(AREA_SIZE, y))

    return {
        "x": x,
        "y": y,
        "speed": speed,
        "direction": direction
    }
