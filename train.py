
#!/usr/bin/env python
"""Train a model using the downloaded data."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the data
data_path = "/data/demand_qty_item_loc.xlsx"
df = pd.read_excel(data_path)

# Prepare features and target
X = df[["item", "loc"]]
y = df["demand_qty"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "/model/trained_model.pkl")
