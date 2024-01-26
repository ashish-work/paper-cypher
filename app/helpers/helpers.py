from pathlib import Path

def get_file_path(file_name):
    # Get the absolute path of the file using Path
    absolute_path = Path(file_name).resolve()

    return absolute_path
