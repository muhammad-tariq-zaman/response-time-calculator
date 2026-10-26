import csv, sys
from datetime import datetime
FMT = "%Y-%m-%d %H:%M"
def avg_minutes(rows):
    deltas = []
    for r in rows:
        deltas.append((datetime.strptime(r["resolved_at"], FMT) - datetime.strptime(r["created_at"], FMT)).total_seconds() / 60)
    return round(sum(deltas) / len(deltas), 1) if deltas else 0.0
def avg_from_csv(path):
    with open(path, newline="", encoding="utf-8") as f: return avg_minutes(list(csv.DictReader(f)))
if __name__ == "__main__":
    print(f"Average resolution time: {avg_from_csv(sys.argv[1])} minutes")
