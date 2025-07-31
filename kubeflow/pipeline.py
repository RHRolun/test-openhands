
import os
import wget
import pandas as pd
from sklearn.linear_model import LinearRegression
from kfp import dsl
from kfp.dsl import InputArtifact, OutputArtifact

@dsl.pipeline(name="Demand Forecasting Pipeline")
def demand_forecasting_pipeline(
    data_url: str = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
):
    """Pipeline for demand forecasting"""

    # Step 1: Download dataset
    download_dataset_op = download_dataset(data_url)

    # Step 2: Preprocess data
    preprocess_data_op = preprocess_data(
        input_data_path=download_dataset_op.outputs['output']
    )

    # Step 3: Train model
    train_model_op = train_model(
        preprocessed_data_path=preprocess_data_op.outputs['output']
    )

    return train_model_op

def download_dataset(data_url: str) -> str:
    """Download dataset from URL"""
    try:
        filename = wget.download(data_url)
        return filename
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        return None

def preprocess_data(input_data_path: str) -> str:
    """Preprocess the dataset"""
    try:
        # Ensure we're working with absolute paths
        input_data_path = os.path.abspath(input_data_path)
        df = pd.read_excel(input_data_path)

        # Preprocessing steps
        df.dropna(inplace=True)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        # Save preprocessed data
        output_path = os.path.join('/workspace/kubeflow', 'preprocessed_data.csv')
        df.to_csv(output_path, index=True)
        return output_path
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

def train_model(preprocessed_data_path: str) -> str:
    """Train the model"""
    try:
        # Ensure we're working with absolute paths
        preprocessed_data_path = os.path.abspath(preprocessed_data_path)

        # Load preprocessed data
        df = pd.read_csv(preprocessed_data_path)

        # Split into features and target
        X = df.drop('demand_qty', axis=1)
        y = df['demand_qty']

        # Train model
        model = LinearRegression()
        model.fit(X, y)

        # Save model
        output_path = os.path.join('/workspace/kubeflow', 'model.pkl')
        with open(output_path, 'wb') as f:
            pickle.dump(model, f)

        return output_path
    except Exception as e:
        print(f"Error training model: {e}")
        return None
