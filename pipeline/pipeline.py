
import kfp
from kfp import dsl
from kfp.dsl import Input, Output, Artifact, component
import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

# Define the URL for the dataset
DATASET_URL = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"

@component(
    base_image="python:3.9",
    packages_to_install=[
        "pandas",
        "scikit-learn",
        "openpyxl",
        "requests"
    ]
)
def download_dataset(
    dataset_url: str,
    output_dataset: Output[Artifact]
):
    """Download the dataset from the given URL"""
    import requests
    import pandas as pd

    # Download the file
    response = requests.get(dataset_url)
    response.raise_for_status()

    # Save the file
    output_path = output_dataset.path + ".xlsx"
    with open(output_path, 'wb') as f:
        f.write(response.content)

    # Update the artifact path to include the .xlsx extension
    output_dataset.path = output_path
    print(f"Dataset downloaded and saved to {output_path}")

@component(
    base_image="python:3.9",
    packages_to_install=[
        "pandas",
        "scikit-learn",
        "joblib",
        "openpyxl"
    ]
)
def train_model(
    input_dataset: Input[Artifact],
    model_output: Output[Artifact]
):
    """Train a model on the downloaded dataset"""
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    import joblib

    # Read the Excel file
    df = pd.read_excel(input_dataset.path)

    # Basic data preprocessing
    # Assuming the dataset has columns that can be used for prediction
    # We'll use a simple approach: use all numeric columns except the target
    # For this example, let's assume 'demand_qty' is the target variable
    target_col = 'demand_qty'

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    # Remove target column from features if it exists
    if target_col in numeric_cols:
        feature_cols = [col for col in numeric_cols if col != target_col]
    else:
        # If target column doesn't exist, use all numeric columns and create a dummy target
        feature_cols = numeric_cols
        df[target_col] = df[feature_cols[0]] if feature_cols else 0  # Use first feature as target

    # Check if we have features and target
    if len(feature_cols) == 0:
        raise ValueError("No numeric features found in the dataset")

    X = df[feature_cols]
    y = df[target_col]

    # Handle missing values
    X = X.fillna(X.mean())
    y = y.fillna(y.mean())

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    model_path = model_output.path + ".joblib"
    joblib.dump(model, model_path)

    # Update the artifact path
    model_output.path = model_path

    # Calculate and print some metrics
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    print(f"Training R² score: {train_score:.4f}")
    print(f"Test R² score: {test_score:.4f}")
    print(f"Model saved to {model_path}")

@dsl.pipeline(
    name="Demand Forecasting Pipeline",
    description="A pipeline to download demand data and train a forecasting model"
)
def forecasting_pipeline(
    dataset_url: str = DATASET_URL
):
    """Pipeline to download dataset and train model"""
    download_task = download_dataset(
        dataset_url=dataset_url
    )

    train_task = train_model(
        input_dataset=download_task.outputs["output_dataset"]
    )

if __name__ == "__main__":
    # Compile the pipeline
    kfp.compiler.Compiler().compile(
        pipeline_func=forecasting_pipeline,
        package_path="forecasting_pipeline.yaml"
    )
