import os
import zipfile

def extract_zip_recursively(zip_path, output_folder):
    """
    Extracts the contents of a zip file, including nested zip files, recursively.

    :param zip_path: Path to the zip file to extract.
    :param output_folder: Folder where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    # Iterate through extracted files to check for nested zips
    for root, _, files in os.walk(output_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if zipfile.is_zipfile(file_path):
                nested_output_folder = os.path.splitext(file_path)[0]
                os.makedirs(nested_output_folder, exist_ok=True)

                # Recursively extract the nested zip
                extract_zip_recursively(file_path, nested_output_folder)

                # Optionally, remove the original nested zip file
                os.remove(file_path)

if __name__ == "__main__":
    input_zip = "312-Furniture.zip"  # Path to your main zip file
    output_directory = "out"  # Directory where all files will be extracted

    os.makedirs(output_directory, exist_ok=True)
    extract_zip_recursively(input_zip, output_directory)
    print(f"All files extracted to {output_directory}")
