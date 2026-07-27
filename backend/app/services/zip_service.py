import zipfile
import os

UPLOAD_FOLDER = "app/uploads"

def extract_zip(zip_path):

    extract_folder = os.path.splitext(zip_path)[0]

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    return extract_folder