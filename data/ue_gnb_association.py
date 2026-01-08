import numpy as np
def get_serving_gnb(x, y, gnb_positions):
    """
    Determine the serving gNB for a given UE based on the closest distance.

    Parameters:
    ue_position (tuple): A tuple (x, y) representing the UE's position.
    gnb_positions (list): A list of tuples [(x1, y1), (x2, y2), ...] representing gNB positions.

    Returns:
    int: Index of the serving gNB in the gnb_positions list.
    """
    min_distance = float('inf')
    serving_gnb_index = -1

    for index, (gnb_x, gnb_y) in gnb_positions.items():
        distance = np.sqrt((x - gnb_x) ** 2 + (y - gnb_y) ** 2)
        if distance < min_distance:
            min_distance = distance
            serving_gnb_index = index
    return serving_gnb_index
