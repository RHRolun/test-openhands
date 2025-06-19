
import kfp
from kfp import dsl
from kfp.components import InputArtifact, OutputArtifact

@dsl.component
def download_dataset(url: str, output_path: OutputArtifact['Excel']) -> None:
    """Download dataset from URL"""

import requests
from pathlib import Path
import os

url = url
output_path = output_path.path

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Download the file
response = requests.get(url)
if response.status_code == 200:
    with open(output_path, 'wb') as f:
        f.write(response.content)
else:
    raise ValueError(f"Failed to download file: {response.status_code}")


@dsl.component
def preprocess_data(input_path: InputArtifact['Excel'], output_path: OutputArtifact['CSV']) -> None:
    """Preprocess dataset"""
    import pandas as pd
    df = pd.read_excel(input_path.path)
    df.to_csv(output_path.path, index=False)

@dsl.component
def train_model(input_path: InputArtifact['CSV'], output_path: OutputArtifact['Model']) -> None:
    """Train model"""
    from sklearn.ensemble import RandomForestRegressor
    import pandas as pd
    df = pd.read_csv(input_path.path)
    # Assume we have features and target columns
    features = df.drop('demand_qty', axis=1)
    target = df['demand_qty']
    model = RandomForestRegressor()
    model.fit(features, target)
    # Save model
    import joblib
    joblib.dump(model, output_path.path)

@dsl.pipeline(name='Demand Forecasting Pipeline')
def pipeline():
    download_step = download_dataset(
        url='https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx',
        output_path=dsl.OutputArtifact('data.xlsx')
    )

    preprocess_step = preprocess_data(
        input_path=download_step.outputs['Excel'],
        output_path=dsl.OutputArtifact('data.csv')
    )

    train_step = train_model(
        input_path=preprocess_step.outputs['CSV'],
        output_path=dsl.OutputArtifact('model.pkl')
    )

if __name__ == '__main__':
    kfp.run(pipeline_func=pipeline,
            pipeline_args=kfp.RunnerArgs())
