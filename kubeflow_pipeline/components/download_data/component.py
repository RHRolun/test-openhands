
import requests
import os
from kfp.components import InputPath, OutputPath

def download_data(url: str, output_path: OutputPath('')):
    """Download data from the given URL and save it."""
    response = requests.get(url)
    response.raise_for_status()

    file_path = os.path.join(output_path, 'data.xlsx')
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_path

def test_download_data():
    """Test the download_data function."""
    test_url = "https://github.com/RHRolun/simple-training-pipeline/raw/refs/heads/main/data/demand_qty_item_loc.xlsx"
    output_path = "test_output"
    os.makedirs(output_path, exist_ok=True)

    result = download_data(test_url, output_path)
    assert os.path.exists(os.path.join(output_path, "data.xlsx")), "Data file was not downloaded"
