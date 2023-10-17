# ChronoShift

A sleek utility designed to effortlessly adjust file and directory timestamps. Whether you're looking to synchronize your files' dates or rewind them to a specific moment, ChronoShift has got you covered.

## Features

1. **Adjust Timestamps**: Easily modify the timestamp of specific files or directories based on the given date.

2. **Recursive Traversal**: The ability to recursively go through directories and modify timestamps for all contained files.

3. **Backup & Restore**:
   - Backup original timestamps prior to changes, saving them in a `backup_timestamps.json` file.
   - Use the `--restore` flag to revert back to original timestamps using the backup.

4. **Stealth Mode**:
   - Enable stealth mode with `-s` or `--stealth`.
   - In stealth mode, there's no console output and backup file isn't created.

5. **File Pattern Matching**:
   - Use `-m` or `--mask` to specify a file pattern (e.g., *.log).
   - Modify timestamps only for files matching the given pattern.

## Usage

```bash
python chronoshift.py -p [TARGET_PATH] -t [DESIRED_DATE] [OPTIONS]
[TARGET_PATH]: The file or directory whose timestamp you want to modify.
[DESIRED_DATE]: The new date for the file/directory in MM/DD/YYYY format.
[OPTIONS]: Additional flags such as -r for recursive, -s for stealth mode, etc.
```
Examples
Modify a single file's timestamp:

```bash
python chronoshift.py -p /path/to/file.txt -t 01/01/2022
Modify timestamps for all .log files in a directory (and sub-directories):
```

```bash
python chronoshift.py -p /path/to/directory -t 01/01/2021 -m *.log -r
Restore original timestamps from backup:
```

```bash
python chronoshift.py --restore
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
