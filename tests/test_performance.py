import pytest
from src.homeworkcsv.reports.performance import generate_performance_report


def test_performance_report_calculation():
    # Подготовка данных (Mock data)
    input_data = [
        {"position": "Dev", "performance": "5.0"},
        {"position": "Dev", "performance": "3.0"},
        {"position": "Manager", "performance": "4.0"},
    ]

    # Действие
    result = generate_performance_report(input_data)

    # Проверка
    # Ожидаем:
    # Dev: (5+3)/2 = 4.0
    # Manager: 4.0
    # Сортировка: одинаковая, порядок не важен или по алфавиту,
    # но главное проверить цифры.

    expected_header = ["Position", "Average Performance"]
    assert result[0] == expected_header

    result_dict = {row[0]: row[1] for row in result[1:]}

    assert result_dict["Dev"] == "4.00"
    assert result_dict["Manager"] == "4.00"


def test_performance_sorting():
    input_data = [
        {"position": "Low", "performance": "2.0"},
        {"position": "High", "performance": "5.0"},
    ]
    result = generate_performance_report(input_data)

    assert result[1][0] == "High"
    assert result[2][0] == "Low"