

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from kfp.components import InputPath, OutputPath
import joblib

def train_model(
    input_data_path: InputPath('DataFrame'),
    output_model_path: OutputPath('model'),
    output_metrics_path: OutputPath('metrics')
):
    """Train a model using the downloaded data."""
    # Read the CSV file
    data = pd.read_csv(str(input_data_path))

    # Preprocess the data
    # (Add any necessary preprocessing steps here)

    # Split the data into features and target
    X = data.drop('demand_qty', axis=1)
    y = data['demand_qty']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # Save the model and metrics
    joblib.dump(model, str(output_model_path))
    with open(str(output_metrics_path), 'w') as f:
        f.write(f"Mean Squared Error: {mse}")

