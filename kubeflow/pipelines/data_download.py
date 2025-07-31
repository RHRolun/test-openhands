
import requests
import pandas as pd
from kfp.components import InputPath, OutputPath

def download_data(
    dataset_url: str,
    output_data_path: OutputPath('DataFrame')
):
    """Download data from URL and save as CSV."""
    response = requests.get(dataset_url)
    data = pd.read_excel(response.content)
    data.to_csv(str(output_data_path), index=False)
