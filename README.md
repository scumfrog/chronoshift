# ChronoShift

A sleek utility designed to effortlessly adjust file and directory timestamps. Whether you're looking to synchronize your files' dates or rewind them to a specific moment, ChronoShift has got you covered.

## Features

- Adjust individual file timestamps with precision.
- Recursively update timestamps across directories.
- Modern and intuitive command-line interface.
- Supports custom date formats.

## Installation

1. Clone the repository:

`git clone https://github.com/scumfrog/chronoshift.git`

2. Navigate to the project directory:

`cd chronoshift`

## Usage

```
python chronoshift.py -p /path/to/target -t MM/DD/YYYY [-r]

- `-p, --path`: Target directory or file for timestamp adjustment.
- `-t, --timestamp`: Desired date in format MM/DD/YYYY for adjustment.
- `-r, --recursive`: If set, will traverse directories recursively.
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
