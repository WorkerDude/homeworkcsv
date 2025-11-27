from csv import DictReader
from pathlib import Path

def read_data(file_path: Path) -> list[dict]:
    with file_path.open("r", encoding="utf-8") as f:
        reader = DictReader(f)
        return list(reader)