from collections import defaultdict

def generate_performance_report(data: list[dict]) -> list[list]:
    position_performance = defaultdict(list)
    for row in data:
        position = row["position"]
        performance = float(row["performance"])
        position_performance[position].append(performance)

    averages = []
    for position, performances in position_performance.items():
        avg = sum(performances) / len(performances)
        averages.append((position, avg))

    averages.sort(key=lambda x: x[1], reverse=True)

    return [["Position", "Average Performance"]] + [[pos, f"{avg:.2f}"] for pos, avg in averages]