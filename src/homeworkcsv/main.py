import argparse
import sys
from pathlib import Path
from tabulate import tabulate
from .data_reader import read_data
from .reports import generate_report


def main():
    parser = argparse.ArgumentParser(description="Generate reports from developer data files.")
    parser.add_argument("--files", nargs="+", required=True, help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Name of the report to generate")

    args = parser.parse_args()

    data = []
    try:
        for file_path_str in args.files:
            path = Path(file_path_str)
            if not path.exists():
                print(f"Error: File not found: {file_path_str}", file=sys.stderr)
                sys.exit(1)

            file_data = read_data(path)
            data.extend(file_data)

        report_data = generate_report(data, args.report)

        headers = report_data[0]
        rows = report_data[1:]
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()