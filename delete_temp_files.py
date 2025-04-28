import os
import shutil

def delete_temp_files(directory, extensions=None):
    """
    Deletes temporary files in the specified directory.

    Args:
        directory (str): The directory to scan for temporary files.
        extensions (list): List of file extensions to delete (e.g., ['.tmp', '.log']).
                           If None, deletes files with common temp extensions.
    """
    if extensions is None:
        extensions = ['.tmp', '.log', '.bak', '.temp']

    deleted_files = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_files += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

    print(f"Total files deleted: {deleted_files}")

if __name__ == "__main__":
    # Example usage
    target_directory = input("Enter the directory to clean up: ")
    if os.path.exists(target_directory):
        delete_temp_files(target_directory)
    else:
        print("Directory does not exist.")