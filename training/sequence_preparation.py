import numpy as np
import pandas as pd

SEQUENCE_LENGTH = 10

def create_sequences(df):
    X = []
    y = []
    df = df.sort_values(by=["ue_id", "time"]) # Double check data is sorted by UE and time.

    for ue_id, ue_data in df.groupby("ue_id"):
        properties = ue_data[["x", "y", "speed", "direction"]].values
        known_target = ue_data["serving_gnb_index"].values

        for i in range(len(properties) - SEQUENCE_LENGTH):
            X.append(properties[i:i+SEQUENCE_LENGTH])
            y.append(known_target[i+SEQUENCE_LENGTH])

    return np.array(X), np.array(y)

if __name__ == "__main__":
    df = pd.read_csv("../data/mobility_traces.csv")
    X, y = create_sequences(df)

    np.save("X.npy", X)
    np.save("y.npy", y)

    print("Training sequences saved")