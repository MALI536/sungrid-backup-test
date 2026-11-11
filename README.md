# Backup and Recovery Test for SunGrid Solar

## Overview
SunGrid Solar installs residential solar panels. The company needs a simple,
low-cost and well-documented way to back up its project files and client data.
This project builds a basic backup process, tests restoring the data, and
documents everything clearly.

## Goals
- Create a working backup script (backup.sh)
- Test restoring data with a restore script (restore.sh)
- Document the results in a test report (report.md)
- Publish the documentation with GitHub Pages

## Repository Contents
- README.md - project overview
- backup_plan.md - scope, schedule and data types to protect
- backup.sh - backup script (Task 2)
- restore.sh - restore script (Task 3)
- report.md - restore test report (Task 3)

## Project Info
- Author: Muhammad Ali
- Technology: Cyber Security
- Duration: 09 Nov 2026 - 15 Nov 2026

## Task 2: Sample Data and Backup Script

### Generate sample data
Creates three CSV files in `sample_data/`:

```bash
py generate_data.py
```

### Run the backup
Copies `sample_data/` into `backup/` and checks the copies match:

```bash
chmod +x backup.sh
./backup.sh
```

### Expected result
`backup/` contains `installations.csv`, `equipment_log.csv` and `maintenance_log.csv`.