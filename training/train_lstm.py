import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

X = np.load("X.npy")
y = np.load("y.npy")

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=64)

class MobilityLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)
        return self.fc(hidden[-1])

model = MobilityLSTM(
    input_size=X.shape[2],
    hidden_size=64,
    num_classes=len(torch.unique(y))
)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    model.train()
    total_loss = 0
    for xb, yb in train_loader:
        optimizer.zero_grad()
        loss = criterion(model(xb), yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss {total_loss:.3f}")

model.eval()
correct = total = 0
with torch.no_grad():
    for xb, yb in test_loader:
        preds = torch.argmax(model(xb), dim=1)
        correct += (preds == yb).sum().item()
        total += yb.size(0)

print(f"Test Accuracy: {100 * correct / total:.2f}%")
