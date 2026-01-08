# ai-mobility-6g

Lightweight scaffold for UE mobility prediction (6G research experiments).

Structure
- `data/` — data generation and raw traces
- `models/` — model definitions (LSTM + baseline)
- `training/` — training and evaluation scripts
- `results/` — output plots and metrics
- `docs/` — architecture and design notes

Quick start
1. Create a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Generate a small mobility dataset and run a quick training pass:

   python data/generate_mobility.py
   python training/train.py

Notes
- This is a scaffold with minimal starter code; replace placeholders with your datasets and experiment settings.