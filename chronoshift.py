import argparse
from datetime import datetime
from pathlib import Path

def update_timestamp(file_path: Path, date_format: str) -> None:
    """Updates the timestamp of the given file."""
    try:
        timestamp = datetime.strptime(date_format, "%m/%d/%Y").timestamp()
        file_path.touch(exist_ok=True, times=(timestamp, timestamp))
        print(f"Timestamp of {file_path} updated to {date_format}")
    except Exception as e:
        print(f"Error updating timestamp for {file_path}: {e}")

def process_files(directory_path: Path, date_format: str, recursive: bool) -> None:
    """Processes files in the directory based on the recursive flag."""
    if recursive:
        for file in directory_path.rglob('*'):
            if file.is_file():
                update_timestamp(file, date_format)
    else:
        for file in directory_path.iterdir():
            if file.is_file():
                update_timestamp(file, date_format)

def main():
    parser = argparse.ArgumentParser(description='Utility to adjust file and directory date marks.')
    parser.add_argument('-p', '--path', required=True, help='Target directory or file for timestamp adjustment.')
    parser.add_argument('-t', '--timestamp', required=True, help='Desired date in format MM/DD/YYYY for adjustment.')
    parser.add_argument('-r', '--recursive', action='store_true', help='If set, will traverse directories recursively.')

    args = parser.parse_args()
    target_path = Path(args.path)

    if not target_path.exists():
        print(f"Error: The provided path {target_path} does not exist.")
        return

    if target_path.is_dir():
        process_files(target_path, args.timestamp, args.recursive)
    else:
        update_timestamp(target_path, args.timestamp)

if __name__ == "__main__":
    main()
