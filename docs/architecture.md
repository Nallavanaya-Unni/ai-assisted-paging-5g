# Architecture

This repository is a scaffold for mobility prediction experiments.

Components:
- **data/**: generators and raw trace CSVs
- **models/**: model definitions (LSTM predictor, baselines)
- **training/**: training and evaluation scripts using PyTorch
- **results/**: training outputs, plots, and metrics

The LSTM model consumes sequences of (x, y) positions and predicts the next (x, y). Replace the dataset handling and model hyperparameters to match your experimental needs.