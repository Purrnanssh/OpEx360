"""Sample operations log generator for OpEx360
Generates a CSV with columns: timestamp, department, process_step, transaction_id, cost, duration_seconds, sla_target_seconds, status
"""
import csv
from datetime import datetime, timedelta
import random

DEPARTMENTS = ["Finance", "Operations", "HR", "Sales", "Support"]
PROCESS_STEPS = ["Receive", "Validate", "Approve", "Execute", "Close"]

random.seed(42)

def generate_rows(n=1000, start_date=datetime(2025, 1, 1)):
    rows = []
    for i in range(n):
        ts = start_date + timedelta(minutes=random.randint(0, 60 * 24 * 90))
        dept = random.choice(DEPARTMENTS)
        step = random.choice(PROCESS_STEPS)
        tid = f"T{100000 + i}"
        cost = round(random.uniform(0.5, 50.0), 2)
        duration = random.randint(10, 3600)  # seconds
        sla = random.choice([300, 600, 1800])
        status = "OK" if duration <= sla else "BREACH"
        rows.append([ts.isoformat(), dept, step, tid, cost, duration, sla, status])
    return rows

if __name__ == '__main__':
    rows = generate_rows(2000)
    header = ["timestamp", "department", "process_step", "transaction_id", "cost", "duration_seconds", "sla_target_seconds", "status"]
    with open('data/sample_operations_log.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print('Generated data/sample_operations_log.csv (2000 rows)')