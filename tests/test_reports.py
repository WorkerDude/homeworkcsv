import pytest
from homeworkcsv.reports import generate_report

def test_generate_report_unknown():
    with pytest.raises(ValueError, match="Unknown report"):
        generate_report([], "super_secret_report")