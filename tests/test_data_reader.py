import pytest
from pathlib import Path
from src.homeworkcsv.data_reader import read_data

@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    content = """name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django, PostgreSQL, Docker",API Team,5
"""
    file_path = tmp_path / "test.csv"
    file_path.write_text(content, encoding="utf-8")
    return file_path

def test_read_data(sample_csv: Path):
    data = read_data(sample_csv)
    assert len(data) == 1
    assert data[0]["name"] == "Alex Ivanov"
    assert data[0]["performance"] == "4.8"

def test_read_data_invalid_file():
    with pytest.raises(FileNotFoundError):
        read_data(Path("nonexistent.csv"))