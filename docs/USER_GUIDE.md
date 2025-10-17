# User Guide

Welcome to the Super Rouge Hunter Marketplace! This guide will help you get started with installing and using plugins.

## What is the Super Rouge Hunter Marketplace?

The Super Rouge Hunter Marketplace is a collection of plugins designed for red team operations, penetration testing, and security research. These plugins extend the capabilities of Claude Code and other development tools with specialized security testing functionality.

## Prerequisites

- Python 3.7 or higher
- Git
- Appropriate permissions for security testing tools
- Authorization to perform security testing on target systems

## Installation

### 1. Clone the Marketplace

```bash
git clone https://github.com/macaugh/super-rouge-hunter-marketplace.git
cd super-rouge-hunter-marketplace
```

### 2. Make the Plugin Manager Executable

```bash
chmod +x scripts/plugin-manager.py
```

### 3. (Optional) Add to PATH

```bash
# Add to your ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/super-rouge-hunter-marketplace/scripts"
```

## Using the Plugin Manager

The plugin manager (`plugin-manager.py`) is your main tool for discovering, installing, and managing plugins.

### List Available Plugins

View all plugins in the marketplace:

```bash
python scripts/plugin-manager.py list
```

Filter by category:

```bash
python scripts/plugin-manager.py list reconnaissance
```

### Search for Plugins

Search by name, description, or tags:

```bash
python scripts/plugin-manager.py search credentials
python scripts/plugin-manager.py search network
```

### View Plugin Information

Get detailed information about a specific plugin:

```bash
python scripts/plugin-manager.py info network-scanner
```

### Install a Plugin

Install a plugin to your local environment:

```bash
python scripts/plugin-manager.py install network-scanner
```

### List Installed Plugins

View all installed plugins:

```bash
python scripts/plugin-manager.py installed
```

### Uninstall a Plugin

Remove an installed plugin:

```bash
python scripts/plugin-manager.py uninstall network-scanner
```

## Using Plugins

After installing a plugin, you can use it directly. Each plugin has its own usage instructions.

### Example: Network Scanner

```bash
# Quick scan
python plugins/network-scanner/scanner.py quick 192.168.1.1

# Full scan
python plugins/network-scanner/scanner.py full 192.168.1.1

# Stealth scan
python plugins/network-scanner/scanner.py stealth 192.168.1.1
```

### Example: Payload Generator

```bash
# Generate reverse shell
python plugins/payload-generator/generator.py reverse 10.10.10.10 4444 linux

# Generate meterpreter payload
python plugins/payload-generator/generator.py meterpreter 10.10.10.10 4444 windows
```

### Example: Credential Harvester

```bash
# Extract browser passwords
python plugins/credential-harvester/harvester.py browser chrome

# Scan memory for credentials
python plugins/credential-harvester/harvester.py memory

# Search files for credentials
python plugins/credential-harvester/harvester.py files /home/user
```

## Plugin Categories

Plugins are organized into the following categories:

- **reconnaissance** - Information gathering and network discovery
- **exploitation** - Exploiting vulnerabilities and gaining access
- **persistence** - Maintaining access to compromised systems
- **privilege-escalation** - Elevating privileges on target systems
- **defense-evasion** - Avoiding detection by security tools
- **credential-access** - Extracting and cracking credentials
- **discovery** - Learning about target environments
- **lateral-movement** - Moving through networks
- **collection** - Gathering data of interest
- **exfiltration** - Extracting data from targets
- **command-and-control** - C2 infrastructure and communication
- **impact** - Disruption and destruction capabilities
- **utilities** - General-purpose tools

## Best Practices

### 1. Always Get Authorization

**NEVER** use these tools without explicit written authorization from the system owner. Unauthorized use is illegal and unethical.

### 2. Document Your Testing

- Keep detailed logs of all activities
- Document authorization and scope
- Record findings systematically

### 3. Stay Updated

```bash
cd super-rouge-hunter-marketplace
git pull origin main
```

### 4. Review Plugin Documentation

Each plugin has its own README with:
- Detailed usage instructions
- Configuration options
- Requirements and dependencies
- Security considerations

### 5. Test in Safe Environments

- Use isolated lab environments
- Test on your own systems first
- Verify functionality before operational use

## Troubleshooting

### Plugin Won't Install

1. Check if Python 3.7+ is installed: `python3 --version`
2. Ensure you have proper permissions
3. Check plugin dependencies in the plugin's README

### Plugin Errors

1. Review the plugin's README for requirements
2. Check if all dependencies are installed
3. Verify you have necessary system permissions
4. Check the plugin's repository for known issues

### Permission Issues

Some plugins require elevated privileges:

```bash
sudo python plugins/plugin-name/script.py [args]
```

## Getting Help

- **Documentation**: Check the plugin's README file
- **Issues**: Open an issue on GitHub
- **Community**: Join discussions in the repository
- **Examples**: Review the example plugins

## Security and Legal Notice

### Important Warnings

⚠️ **Legal Compliance**: These tools must only be used in compliance with all applicable laws and regulations.

⚠️ **Authorization Required**: Always obtain explicit written authorization before testing any system you don't own.

⚠️ **Responsible Use**: These tools are powerful and can cause damage if misused.

### Intended Use Cases

These plugins are designed for:

- Authorized penetration testing engagements
- Red team exercises with proper authorization
- Security research in controlled environments
- Educational purposes in lab settings
- Vulnerability assessment with client approval

### Prohibited Uses

DO NOT use these tools for:

- Unauthorized access to systems
- Malicious attacks
- Criminal activities
- Violating terms of service
- Any illegal purposes

## Contributing

Want to add your own plugin? See the [Plugin Development Guide](PLUGIN_DEVELOPMENT.md).

## License

Individual plugins may have their own licenses. Check each plugin's README for details.

## Support

For questions, issues, or suggestions:

1. Check existing documentation
2. Review closed issues on GitHub
3. Open a new issue with detailed information
4. Provide reproduction steps for bugs

---

**Remember**: With great power comes great responsibility. Use these tools ethically, legally, and responsibly.
