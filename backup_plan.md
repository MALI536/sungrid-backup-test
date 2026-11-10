# Backup Plan

## Scope
**Covered:**
- Project files for solar panel installations
- Client data such as contact details, quotes and contracts

**Not covered:**
- Employees' personal files
- Cloud email accounts

**Responsibility:**
- The IT contact at SunGrid Solar runs and checks the backups.

## Schedule
- **Customer details:** backed up daily at 11:00 PM, because they change often and are critical.
- **Site photos:** backed up weekly on Sunday at 11:00 PM, because they are large and rarely change.
- **Retention:** keep the last 7 daily backups and 4 weekly backups.
- **Storage location:** a local backup folder on a separate drive. An offsite or cloud copy is a future improvement.

## Data Types
| Data type | Approx. size | Sensitivity |
|---|---|---|
| Customer details (names, phones, addresses) | Small (a few MB) | High, personal information |
| Site survey notes and photos | Large (several GB) | Medium |
| Quotes, invoices and contracts | Medium (hundreds of MB) | High, financial and legal |
| Panel layout and installation designs | Medium (hundreds of MB) | Medium |
| Warranty and maintenance records | Small (a few MB) | Medium |
## Security
- **Access:** only the IT contact at SunGrid Solar can open the backup folder.
- **Encryption at rest:** backup files are encrypted on the storage drive.
- **Encryption in transit:** not needed for now, as backups stay on a local drive. When an offsite or cloud copy is added, the transfer will use HTTPS or SFTP.