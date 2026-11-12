# Restore Test Report

- **Project:** SunGrid Solar Backup and Recovery Test
- **Author:** Muhammad Ali
- **Test date:** 12 November 2026
- **Live site:** [https://mali536.github.io/sungrid-backup-test/](https://mali536.github.io/sungrid-backup-test/)
## Purpose
Confirm that files saved by `backup.sh` can be restored correctly, and that the restored files are identical to the originals.

## Environment
- Windows with Git Bash (run inside VS Code)
- Scripts: `backup.sh` and `restore.sh`
- Data: three CSV files in `sample_data/`

## Test steps
1. Run `./backup.sh` to copy `sample_data/` into `backup/`.
2. Run `./restore.sh`, which:
   - checks that `backup/` exists,
   - copies the files from `backup/` into `restore/`,
   - calculates the SHA-256 hash of each original and each restored file and compares them.
3. List the restored files with `ls restore`.

## Results

| File | Restored | Hash match |
|---|---|---|
| equipment_log.csv | Yes | OK |
| installations.csv | Yes | OK |
| maintenance_log.csv | Yes | OK |

Final output: `Restore successful: all files match the originals`

SHA-256 hashes (identical for original and restored copy):

| File | SHA-256 |
|---|---|
| equipment_log.csv | c21ca76f3263071af17c384a5ad7c3e2633516a4ebbfce367645bd5dfbc74c77 |
| installations.csv | 15dd624ff80e0872ae2b715f2621a301782cc7173b7766b53d307e0ea7d177fd |
| maintenance_log.csv | 5da35ab9a8bcb99716cc565d56e14e22559833a1d8f0cba213c03b26af883154 |

## Observations
- All 3 of 3 files were restored with matching hashes, so no data was lost or changed.
- Hash comparison is a stronger check than comparing file names or sizes.
- `restore.sh` stops with an error if `backup/` does not exist, so a missing backup is caught early.
- Files deleted from `sample_data/` after a backup stay in `backup/`, so take a fresh backup before testing.

## Conclusion
The backup and restore process works. Files can be backed up and restored with verified integrity.