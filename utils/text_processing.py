"""
This module contains basic text preprocessing functions, such as cleaning
and formatting text data.

These functions are inspired by common preprocessing needs found in the
original `app.py` project, extracted here to keep preprocessing logic reusable
and separate from the main application.
"""
import re

def clean_text(text):
    """
    Basic text cleaning to remove extra spaces and newlines.

    Parameters:
    - text: The input string to clean.

    Returns:
    - Cleaned text string.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text
