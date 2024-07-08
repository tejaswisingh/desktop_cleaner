import os
import shutil

def move_files(source_dir, target_dir):
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Get a list of all files in the source directory
    file_names = os.listdir(source_dir)

    # Exclude the recycle bin folder (if it exists)
    if "Recycle Bin" in file_names:
        file_names.remove("Recycle Bin")

    # Move each file to the target directory
    for file_name in file_names:
        source_path = os.path.join(source_dir, file_name)
        target_path = os.path.join(target_dir, file_name)
        if os.path.isfile(source_path):  # Only move files (not directories)
            shutil.move(source_path, target_path)

# Usage:
desktop_directory = os.path.expanduser("~/Desktop")  # User's desktop directory
destination_directory = os.path.expanduser("~/Desktop/Desktop")  # Specify your desired destination

move_files(desktop_directory, destination_directory)
print("Files moved successfully!")
