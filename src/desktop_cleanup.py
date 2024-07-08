import os
import shutil
import logging
import datetime

# Set up logging
logging.basicConfig(filename="desktop_cleaner.log", level=logging.INFO, filemode="a")

# Helper Function
def formatted_datetime_to_am_pm():
    datetime_now = datetime.datetime.now()
    return datetime_now.strftime("%d-%m-%Y %I:%M:%S %p")

def move_files(source_dir, target_dir):
    try: 
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
                logging.info(f"{formatted_datetime_to_am_pm()} - Moved: {file_name}.")
    except Exception as e:
        logging.info(f"{formatted_datetime_to_am_pm()} - Error: {e}")


# Usage:
def main():
    desktop_directory = os.path.expanduser("~/Desktop")
    destination_directory = os.path.expanduser("~/Desktop/Desktop")
    move_files(desktop_directory, destination_directory)
    logging.info(f"{formatted_datetime_to_am_pm()} - Files moved successfully!")
    

if __name__ == "__main__":
    main()



