"""
This module contains reusable helper functions for file operations such as
creating directories and saving uploaded files.

These functions are extracted from the original `app.py` source code where
file saving and folder creation happens. By moving them here, the codebase
becomes cleaner and more maintainable.
"""
import os

def ensure_folder_exists(folder_path):
    """Create folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def save_uploaded_file(uploaded_file, upload_folder):
    """
    Save an uploaded file to the specified upload folder.

    Parameters:
    - uploaded_file: File object received in the request.
    - upload_folder: Path to the folder where file will be saved.

    Returns:
    - Full file path of the saved file.
    """
    ensure_folder_exists(upload_folder)
    filepath = os.path.join(upload_folder, uploaded_file.filename)
    uploaded_file.save(filepath)
    return filepath
