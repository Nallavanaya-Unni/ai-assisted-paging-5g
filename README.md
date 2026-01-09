# AI-Assisted Mobility Prediction for Paging Optimization in 5G/6G

## Overview
This project demonstrates how machine learning–based mobility prediction can be used to reduce paging signaling overhead in cellular networks. A realistic UE mobility simulator is combined with an LSTM-based predictor to anticipate the next serving cell of idle UEs.

The predicted mobility information is applied to sequential paging, showing significant reductions in control-plane signaling compared to traditional TA-wide paging.

## Key Contributions
- UE mobility simulator with correlated movement
- LSTM-based next-cell prediction
- Heuristic baselines (last-cell, strongest-signal)
- Quantitative paging reduction analysis
- Standards-aligned interpretation using NWDAF (3GPP TS 23.288)

## Relevance to 5G/6G
This work aligns with ongoing 3GPP efforts on:
- Network Data Analytics Function (NWDAF)
- AI-native network optimization
- Energy-efficient mobility management

## How to Run
1. Generate mobility data
python data/generate_mobility.py
2. Prepare training sequence
python training/prepare_sequences.py
3. Train LSTM model
python training/train_lstm.py
4. Evaluate baselines
python training/baselines.py

## Mapping to 3GPP NWDAF (TS 23.288)

In a real 5G system, the proposed mobility prediction function can be implemented as part of the Network Data Analytics Function (NWDAF). Mobility-related data such as serving cell history, handover frequency, and radio measurements are collected from AMF and RAN nodes.

The NWDAF processes this data to predict the UE’s next serving cell and exposes the analytics to the AMF. The AMF can then apply sequential paging, first paging the predicted cell before falling back to TA-wide paging if needed.

This approach aligns with ongoing 3GPP discussions on analytics-driven mobility management and AI-native core networks.

