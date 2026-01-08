import pandas as pd
from gnb_topology import generate_gnb_positions
from ue_mobility_model import initialize_ue, update_ue_state
from ue_gnb_association import get_serving_gnb

NUM_UES = 100
SIM_TIME = 600

def generate_mobility_traces():
    gnb_positions = generate_gnb_positions()
    traces = []

    for ue_id in range(NUM_UES):
        state = initialize_ue()

        for t in range(SIM_TIME):
            serving_gnb_index = get_serving_gnb(state["x"], state["y"], gnb_positions)

            traces.append({
                "ue_id": ue_id,
                "time": t,
                "x": state["x"],
                "y": state["y"],
                "speed": state["speed"],
                "direction": state["direction"],
                "serving_gnb_index": serving_gnb_index
            })

            state = update_ue_state(state)

    return pd.DataFrame(traces)

if __name__ == "__main__":
    df = generate_mobility_traces()
    df.to_csv("./data/mobility_traces.csv", index=False)
    print("Mobility traces generated successfully.")

