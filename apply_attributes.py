import os
import datetime

def datetime_to_timestamp(dt):
    return int(dt.timestamp())

def apply_attributes(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            file_path, created_time_iso, modified_time_iso, accessed_time_iso = line.strip().split('\t')
            created_time = datetime_to_timestamp(datetime.datetime.fromisoformat(created_time_iso))
            modified_time = datetime_to_timestamp(datetime.datetime.fromisoformat(modified_time_iso))
            accessed_time = datetime_to_timestamp(datetime.datetime.fromisoformat(accessed_time_iso))
            
            os.utime(file_path, (accessed_time, modified_time))

if __name__ == "__main__":
    input_file = "file_attributes.txt"  # Change to the path of your stored attributes file
    apply_attributes(input_file)
