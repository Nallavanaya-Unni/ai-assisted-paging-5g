"""
Place cell towers in a grid layout within a defined area.
Each cell tower is positioned at the center of its respective cell.
Distance between adjacent cell towers is kept consistent.
Total number of cells is NUM_CELLS_X * NUM_CELLS_Y. 
Cells are identified by unique cell IDs (equal to the index of the cell in the list).
"""
import numpy as np

AREA_SIZE = 1000
CELL_SPACING = 250
NUM_CELLS_X = 4
NUM_CELLS_Y = 4

def generate_gnb_positions():
    gnb_positions = {}
    cell_id = 0
    for i in range(NUM_CELLS_X):
        for j in range(NUM_CELLS_Y):
            x = i * CELL_SPACING + CELL_SPACING / 2
            y = j * CELL_SPACING + CELL_SPACING / 2
            gnb_positions[cell_id] = (x, y)
            cell_id += 1

    return gnb_positions