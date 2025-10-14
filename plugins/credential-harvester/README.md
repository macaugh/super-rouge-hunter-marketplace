# Credential Harvester Plugin

Extract and analyze credentials from multiple sources including browsers, memory, and files.

## Features

- **Browser Password Extraction**: Extract saved passwords from Chrome, Firefox, Edge
- **Memory Analysis**: Scan process memory for credentials
- **File Scanning**: Search for credential files (SSH keys, AWS credentials, etc.)
- **Hash Extraction**: Extract password hashes from SAM, shadow files

## Installation

```bash
pip install pycryptodome psutil
```

## Usage

### Browser Passwords
```bash
python harvester.py browser chrome
python harvester.py browser all
```

### Memory Credentials
```bash
python harvester.py memory lsass.exe
```

### File Credentials
```bash
python harvester.py files /home/user
```

### Hash Extraction
```bash
python harvester.py hashes sam
```

## Configuration

Edit `plugin.json` to customize:
- `searchDepth`: Depth of file search (shallow, medium, deep)
- `includeHashes`: Whether to include password hashes
- `outputFormat`: Output format (json, csv, text)

## Security Notice

This tool is for authorized security assessment only. Unauthorized access to credentials is illegal. Always obtain proper authorization and handle extracted credentials securely.

## Requirements

- Python 3.7+
- Administrator/Root privileges (for memory and system file access)
- pycryptodome
- psutil
