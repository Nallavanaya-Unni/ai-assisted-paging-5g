import pandas as pd
import numpy as np
from math import sqrt

# Load data
df = pd.read_csv("../data/mobility_traces.csv")
df = df.sort_values(by=["ue_id", "time"])

# Generate cells (same as topology)
cells = {}
cell_id = 0
for i in range(4):
    for j in range(4):
        cells[cell_id] = (i*250 + 125, j*250 + 125)
        cell_id += 1

def nearest_cell(x, y):
    return min(cells, key=lambda c: sqrt((x-cells[c][0])**2 + (y-cells[c][1])**2))

lsc_correct = 0
ss_correct = 0
total = 0

for ue_id, ue in df.groupby("ue_id"):
    ue = ue.reset_index(drop=True)
    for t in range(len(ue)-1):
        total += 1

        # Last Serving Cell
        if ue.loc[t, "serving_gnb_index"] == ue.loc[t+1, "serving_gnb_index"]:
            lsc_correct += 1

        # Strongest Signal
        pred = nearest_cell(ue.loc[t, "x"], ue.loc[t, "y"])
        if pred == ue.loc[t+1, "serving_gnb_index"]:
            ss_correct += 1

print("LSC Accuracy:", lsc_correct / total)
print("Strongest Signal Accuracy:", ss_correct / total)
