# Payload Generator Plugin

Generate and customize exploitation payloads for various platforms and frameworks.

## Features

- **Reverse Shell Generation**: Create reverse shell payloads for multiple platforms
- **Bind Shell Generation**: Generate bind shell payloads
- **Meterpreter Payloads**: Generate Metasploit meterpreter payloads
- **Payload Encoding**: Encode and obfuscate payloads
- **Multi-Platform Support**: Linux, Windows, Python, and more

## Installation

```bash
pip install pycryptodome
```

## Usage

### Reverse Shell
```bash
python generator.py reverse 10.10.10.10 4444 linux
```

### Bind Shell
```bash
python generator.py bind 4444 linux
```

### Meterpreter
```bash
python generator.py meterpreter 10.10.10.10 4444 windows
```

### Encode Payload
```bash
python generator.py encode "payload string" base64
```

## Configuration

Edit `plugin.json` to customize:
- `defaultEncoder`: Default encoding method
- `outputFormat`: Output format (raw, hex, base64)
- `architecture`: Target architecture (x86, x64)

## Security Notice

This tool is for authorized security testing only. Misuse of exploitation payloads is illegal and unethical. Always obtain proper authorization before using these tools.
