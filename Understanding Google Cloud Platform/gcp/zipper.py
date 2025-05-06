import zipfile
import os

def zip_single_file(file_to_zip_path, output_zip_path):
    """
    Creates a zip archive containing a single specified file.

    Args:
        file_to_zip_path (str): The full path to the file you want to zip.
        output_zip_path (str): The full path for the resulting zip archive.
    """
    if not os.path.isfile(file_to_zip_path):
        print(f"Error: The file '{file_to_zip_path}' does not exist or is not a file.")
        return

    try:
        # Create a ZipFile object in write mode ('w')
        # zipfile.ZIP_DEFLATED enables compression
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add the file to the zip archive.
            # os.path.basename() ensures the file is added to the root of the zip
            # without its original directory structure.
            zipf.write(file_to_zip_path, os.path.basename(file_to_zip_path))
        print(f"Successfully zipped '{file_to_zip_path}' to '{output_zip_path}'")
    except FileNotFoundError:
        print(f"Error: Could not find the file '{file_to_zip_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---

# Define the file you want to zip and the name of the output zip file
file_path = r'xyz.json' # Replace with your actual file path
zip_path = r'c:\Users\ASUS\gcp\22f3001477_storage_commands.zip'   # Replace with your desired zip file path

# --- Optional: Create a dummy file for testing if it doesn't exist ---
if not os.path.exists(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write("This is the content of the file to be zipped.\n")
        print(f"Created dummy file for testing: '{file_path}'")
    except Exception as e:
        print(f"Could not create dummy file: {e}")
# --- End Optional Section ---

# Call the function to zip the file
zip_single_file(file_path, zip_path)