
from kubeflow import dsl
import os
from datetime import datetime

@dsl.pipeline(
    name="Demand Forecasting Pipeline",
    description="A pipeline that downloads demand data and trains a forecasting model"
)
def demand_forecasting_pipeline():
    """Pipeline that downloads data and trains a model."""

    # Download data task
    download_data = dsl.ContainerOp(
        name="download_data",
        image="python:3.8",
        command=["python", "-c"],
        arguments=["""
            import pandas as pd
            import requests

            url = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
            response = requests.get(url)
            with open('data/demand_qty_item_loc.xlsx', 'wb') as f:
                f.write(response.content)
        """],
        file_outputs={
            "data_path": "/data/demand_qty_item_loc.xlsx"
        }
    )

    # Train model task
    train_model = dsl.ContainerOp(
        name="train_model",
        image="python:3.8",
        command=["python", "-c"],
        arguments=["""
            import pandas as pd
            import joblib

            # Load data
            data_path = os.getenv('DATA_PATH')
            df = pd.read_excel(data_path)

            # Simple training (example)
            # In a real scenario, implement your training logic here
            model = {'columns': df.columns, 'data': df}
            joblib.dump(model, 'model.pkl')
        """],
        inputs={
            "data_path": download_data.outputs["data_path"]
        },
        file_outputs={
            "model_path": "/model.pkl"
        }
    )

if __name__ == "__main__":
    dsl.run(pipeline_func=demand_forecasting_pipeline, arguments={})
