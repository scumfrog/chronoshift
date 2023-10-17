import os
import datetime
import argparse
from pathlib import Path
import json
import fnmatch

def update_timestamp(filepath, timestamp):
    if filepath.exists():
        original_timestamp = filepath.stat().st_mtime
        backup_data[str(filepath)] = original_timestamp

        new_timestamp_sec = datetime.datetime.strptime(timestamp, "%m/%d/%Y").timestamp()
        os.utime(filepath, (new_timestamp_sec, new_timestamp_sec))

        if not stealth_mode:
            print(f"Timestamp of {filepath} updated to {timestamp}.")

def process_files(directory, timestamp, mask="*", recursive=True):
    for file in directory.iterdir():
        if file.is_file() and fnmatch.fnmatch(file.name, mask):
            update_timestamp(file, timestamp)
        elif file.is_dir() and recursive:
            process_files(file, timestamp, mask)

backup_data = {}
stealth_mode = False

def main():
    parser = argparse.ArgumentParser(description="Utility to adjust file and directory date marks.")
    parser.add_argument("-p", "--path", required=True, help="Target directory or file for timestamp adjustment.")
    parser.add_argument("-t", "--timestamp", required=True, help="Desired date in format MM/DD/YYYY for adjustment.")
    parser.add_argument("-r", "--recursive", action="store_true", help="If set, will traverse directories recursively.")
    parser.add_argument("-s", "--stealth", action="store_true", help="Enable stealth mode: No output messages and no backup file.")
    parser.add_argument("-m", "--mask", default="*", help="File pattern or mask to match (e.g., *.log).")
    parser.add_argument("--restore", action="store_true", help="Restore file timestamps from backup.")

    args = parser.parse_args()
    global stealth_mode
    stealth_mode = args.stealth

    target_path = Path(args.path)

    if args.restore:
        with open("backup_timestamps.json", "r") as file:
            backup_data = json.load(file)

        for path_str, original_timestamp in backup_data.items():
            os.utime(path_str, (original_timestamp, original_timestamp))

        if not stealth_mode:
            print("Timestamps restored from backup.")
        return

    if not target_path.exists():
        print(f"Error: The provided path {target_path} does not exist.")
        return

    if target_path.is_dir():
        process_files(target_path, args.timestamp, args.mask, args.recursive)
    else:
        if fnmatch.fnmatch(target_path.name, args.mask):
            update_timestamp(target_path, args.timestamp)

    if not stealth_mode:
        with open("backup_timestamps.json", "w") as file:
            json.dump(backup_data, file)

if __name__ == "__main__":
    main()
