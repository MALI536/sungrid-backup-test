#!/bin/bash
# backup.sh - Backs up the SunGrid Solar sample data to a backup folder

# Stop the script immediately if any command fails
set -e

# Folder to back up, and where the copies will go
SRC="sample_data"
DEST="backup"

# Step 1: Create the backup folder if it doesn't exist yet
mkdir -p "$DEST"

# Step 2: Copy all files from sample_data/ into backup/
# -r copies folders recursively, -p keeps timestamps and permissions
cp -rp "$SRC"/. "$DEST"/

# Step 3: Confirm the backup worked by comparing both folders
if diff -r "$SRC" "$DEST" > /dev/null; then
    echo "Backup successful: $(ls "$DEST" | wc -l) files copied to $DEST/"
else
    echo "Backup FAILED: files do not match"
    exit 1
fi

# Step 4: Show the backed-up files and the time of the backup
ls "$DEST"
echo "Backup completed at $(date)"