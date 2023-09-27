import os
import datetime

def capture_attributes(directory):
    with open('file_attributes.txt', 'w') as file:
        for root, _, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                created_time = os.path.getctime(file_path)
                modified_time = os.path.getmtime(file_path)
                accessed_time = os.path.getatime(file_path)
                
                # Convert timestamps to ISO format
                created_time_iso = datetime.datetime.fromtimestamp(created_time).isoformat()
                modified_time_iso = datetime.datetime.fromtimestamp(modified_time).isoformat()
                accessed_time_iso = datetime.datetime.fromtimestamp(accessed_time).isoformat()
                
                # Write to the file
                file.write(f"{file_path}\t{created_time_iso}\t{modified_time_iso}\t{accessed_time_iso}\n")

if __name__ == "__main__":
    source_directory = "."  # Change to your source directory
    capture_attributes(source_directory)
