# generate_data.py
# Creates three realistic sample CSV files for SunGrid Solar in sample_data/

import csv
import os
import random
from datetime import date, timedelta

random.seed(42)  # same data every run
os.makedirs("sample_data", exist_ok=True)

first = ["Ali", "Sara", "Ahmed", "Fatima", "Usman", "Ayesha", "Bilal", "Hina", "Hamza", "Zainab"]
last = ["Khan", "Malik", "Sheikh", "Butt", "Raza", "Qureshi", "Iqbal", "Hussain", "Shah", "Ahmad"]
cities = ["Rawalpindi", "Islamabad", "Peshawar", "Lahore", "Karachi"]
panels = ["JA Solar JAM72", "Longi Hi-MO 5", "Canadian Solar HiKu", "Trina Vertex"]
inverters = ["Huawei SUN2000", "Growatt MIN 5000", "Solis S6", "Sungrow SG5.0"]
techs = ["Imran", "Kamran", "Nadia", "Tariq"]
issues = ["Inverter fault", "Panel cleaning", "Loose wiring", "Low output", "Monitoring offline"]

def random_date(start_year=2025):
    return date(start_year, 1, 1) + timedelta(days=random.randint(0, 600))

# 1. installations.csv
installs = []
with open("sample_data/installations.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["install_id", "client_name", "city", "panel_count", "system_kw", "install_date", "status"])
    for i in range(1, 21):
        count = random.choice([6, 8, 10, 12, 16])
        installs.append(i)
        w.writerow([f"INS{i:03d}", f"{random.choice(first)} {random.choice(last)}", random.choice(cities),
                    count, round(count * 0.55, 2), random_date(), random.choice(["Completed", "Scheduled", "In Progress"])])

# 2. equipment_log.csv
with open("sample_data/equipment_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["log_id", "install_id", "panel_model", "inverter_model", "serial_number", "warranty_years"])
    for i, ins in enumerate(installs, 1):
        w.writerow([f"EQ{i:03d}", f"INS{ins:03d}", random.choice(panels), random.choice(inverters),
                    f"SN{random.randint(100000, 999999)}", random.choice([5, 10, 25])])

# 3. maintenance_log.csv
with open("sample_data/maintenance_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticket_id", "install_id", "visit_date", "technician", "issue", "resolved"])
    for i in range(1, 16):
        w.writerow([f"TK{i:03d}", f"INS{random.choice(installs):03d}", random_date(2026),
                    random.choice(techs), random.choice(issues), random.choice(["Yes", "No"])])

print("Created 3 CSV files in sample_data/")