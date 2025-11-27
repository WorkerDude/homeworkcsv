from .performance import generate_performance_report

REPORT_GENERATORS = {
    "performance": generate_performance_report,
}

def generate_report(data: list[dict], report_name: str) -> list[list]:
    if report_name not in REPORT_GENERATORS:
        raise ValueError(f"Unknown report: {report_name}")
    return REPORT_GENERATORS[report_name](data)