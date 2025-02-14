"""
    This module calls the Azure ML model endpoint.
"""


import json
import requests

AZURE_ML_ENDPOINT = "https://<azure-ml-endpoint-url>"
API_KEY = "<your-api-key>"


def call_ml_model(input_data: dict):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    response = requests.post(AZURE_ML_ENDPOINT, json=json.dumps(input_data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ML Model call failed: {response.text}")
