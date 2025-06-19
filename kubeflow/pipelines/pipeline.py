

import kubeflow.dsl as dsl
from components.data_download import download_data
from components.model_training import train_model
from kubeflow.dsspec import Op, run_pipeline

@dsl.pipeline(
    name="Demand Forecasting Pipeline",
    description="A pipeline that downloads demand data and trains a forecasting model."
)
def demand_forecasting_pipeline(
    dataset_url: str = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
):
    """Pipeline that downloads data and trains a model."""

    # Download data component
    download_task = download_data(
        dataset_url=dataset_url
    )

    # Train model component
    train_task = train_model(
        input_data_path=download_task.outputs['output_data_path'],
        output_model_path=dsl.OutputPath('model'),
        output_metrics_path=dsl.OutputPath('metrics')
    )

def run_pipeline(args):
    """Run the pipeline with the given arguments."""
    Op.dsspec().add_op(demand_forecasting_pipeline)
    run_pipeline(
        pipeline_func=demand_forecasting_pipeline,
        pipeline_args={
            'dataset_url': args.dataset_url,
        },
        run_name='demand-forecasting-run'
    )

