
from kubeflow import dsl

@dsl.pipeline(
    name="Demand Forecasting Pipeline",
    description="A pipeline that downloads data and trains a model"
)
def demand_forecasting_pipeline():
    """Pipeline that downloads data and trains a model."""

    # Download data task
    download_task = dsl.ContainerOp(
        name="Download Data",
        image="alpine:3.12",
        command=["sh", "-c"],
        arguments=["mkdir -p /data && wget -O /data/demand_qty_item_loc.xlsx https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"],
        file_outputs={
            "data": "/data/demand_qty_item_loc.xlsx"
        }
    )

    # Train model task
    train_task = dsl.ContainerOp(
        name="Train Model",
        image="python:3.10",
        command=["sh", "-c"],
        arguments=[
            "python train.py --data_path /data/demand_qty_item_loc.xlsx"
        ],
        file_inputs={
            "data": download_task.outputs["data"]
        },
        file_outputs={
            "model": "/model/trained_model.pkl"
        }
    )

    download_task >> train_task
