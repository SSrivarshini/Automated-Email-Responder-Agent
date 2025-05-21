"""
This module contains a helper function to load the Hugging Face zero-shot
classification model.

This code is extracted from the original app.py source code to improve
reusability and scalability by modularizing model loading.

The model used is "facebook/bart-large-mnli", which is dynamically loaded
from Hugging Face’s model hub when the Flask app runs. No local model files
are stored in this repository.

To change or update the model, modify the 'model_name' parameter in the
'get_classifier()' function below.
"""

from transformers import pipeline

def get_classifier(model_name="facebook/bart-large-mnli"):
    """
    Loads and returns the zero-shot classification pipeline.

    Parameters:
    - model_name: Hugging Face model identifier (default: "facebook/bart-large-mnli")

    Returns:
    - classifier pipeline object
    """
    return pipeline("zero-shot-classification", model=model_name)
