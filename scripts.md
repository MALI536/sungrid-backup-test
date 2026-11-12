# Scripts

## backup.sh
Copies `sample_data/` into `backup/` and checks the copies match.

```bash
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
```

## restore.sh
Copies `backup/` into `restore/` and verifies each file with a SHA-256 hash.

```bash
#!/bin/bash
# restore.sh - Restores files from backup/ to restore/ and verifies them with SHA-256 hashes

# Stop immediately if any command fails
set -e

SRC="backup"          # where the backup copies are
DEST="restore"        # where files will be restored to
ORIG="sample_data"    # the original files to compare against

# Step 1: Make sure a backup exists
if [ ! -d "$SRC" ]; then
    echo "ERROR: backup/ not found. Run ./backup.sh first."
    exit 1
fi

# Step 2: Create the restore folder and copy the backup files into it
mkdir -p "$DEST"
cp -rp "$SRC"/. "$DEST"/

# Step 3: Compare the SHA-256 hash of every original with its restored copy
FAIL=0
for f in "$ORIG"/*; do
    name=$(basename "$f")
    h1=$(sha256sum "$f" | cut -d' ' -f1)
    h2=$(sha256sum "$DEST/$name" | cut -d' ' -f1)
    if [ "$h1" = "$h2" ]; then
        echo "OK    $name  $h1"
    else
        echo "FAIL  $name"
        FAIL=1
    fi
done

# Step 4: Report the final result
if [ "$FAIL" -eq 0 ]; then
    echo "Restore successful: all files match the originals"
else
    echo "Restore FAILED: some files do not match"
    exit 1
fi
```