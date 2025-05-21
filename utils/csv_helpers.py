"""
This module provides helper functions for handling CSV files with pandas,
such as loading and saving data.

These functions are adapted from CSV operations in the `app.py` code to 
encapsulate the logic separately for better organization.
"""
import pandas as pd

def load_csv(filepath):
    """Load CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)

def save_csv(df, filepath):
    """Save pandas DataFrame to a CSV file."""
    df.to_csv(filepath, index=False)

