# Network Scanner Plugin

Advanced network scanning and reconnaissance plugin for red team operations.

## Features

- **Quick Scan**: Fast scan of common ports
- **Full Scan**: Comprehensive scan with service detection and OS fingerprinting
- **Stealth Scan**: Low-profile SYN scanning to avoid detection
- **Service Detection**: Detailed version detection for specific services

## Installation

```bash
pip install python-nmap scapy
```

## Usage

### Quick Scan
```bash
python scanner.py quick 192.168.1.1
```

### Full Scan
```bash
python scanner.py full 192.168.1.1
```

### Stealth Scan
```bash
python scanner.py stealth 192.168.1.1
```

### Service Detection
```bash
python scanner.py service 192.168.1.1 80
```

## Configuration

Edit `plugin.json` to customize:
- `defaultTimeout`: Scan timeout in seconds
- `defaultPorts`: Port range to scan
- `scanSpeed`: Scanning speed (normal, aggressive, stealth)
- `outputFormat`: Output format (json, xml, text)

## Requirements

- Python 3.7+
- nmap
- masscan (optional)
- Root/Administrator privileges for certain scan types

## Security Notice

This tool is intended for authorized security testing only. Always ensure you have proper authorization before scanning any network or system.
