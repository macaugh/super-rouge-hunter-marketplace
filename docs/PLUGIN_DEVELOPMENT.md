# Plugin Developer Guide

This guide helps you create plugins for the Super Rouge Hunter Marketplace.

## Plugin Structure

Each plugin should have the following structure:

```
plugins/
└── your-plugin-id/
    ├── plugin.json       # Plugin metadata (required)
    ├── README.md         # Plugin documentation (required)
    ├── entrypoint.py     # Main plugin file (or as specified in plugin.json)
    └── [other files]     # Additional plugin files
```

## Plugin Metadata (plugin.json)

Every plugin must have a `plugin.json` file that conforms to the marketplace schema:

```json
{
  "id": "your-plugin-id",
  "name": "Your Plugin Name",
  "version": "1.0.0",
  "description": "Brief description of your plugin",
  "author": "Your Name or Organization",
  "category": "reconnaissance",
  "tags": ["tag1", "tag2", "tag3"],
  "repository": "https://github.com/yourusername/your-plugin",
  "homepage": "https://your-plugin-docs.com",
  "license": "MIT",
  "dependencies": {
    "plugins": ["other-plugin-id"],
    "tools": ["nmap", "curl"],
    "libraries": {
      "python": ["requests", "beautifulsoup4"],
      "nodejs": ["axios", "cheerio"]
    }
  },
  "compatibility": {
    "platforms": ["linux", "macos", "windows"],
    "minVersion": "1.0.0"
  },
  "capabilities": [
    "capability-1",
    "capability-2"
  ],
  "entrypoint": "main.py",
  "configuration": {
    "option1": "default-value",
    "option2": true
  }
}
```

## Required Fields

- **id**: Unique identifier in kebab-case (e.g., `network-scanner`)
- **name**: Human-readable plugin name
- **version**: Semantic version (e.g., `1.0.0`)
- **description**: Brief description of what the plugin does
- **author**: Your name or organization
- **category**: One of the predefined categories (see Categories section)

## Categories

Plugins must be assigned to one of these categories (based on MITRE ATT&CK):

- `reconnaissance` - Information gathering and discovery
- `exploitation` - Exploiting vulnerabilities
- `persistence` - Maintaining access to systems
- `privilege-escalation` - Elevating privileges
- `defense-evasion` - Avoiding detection
- `credential-access` - Stealing credentials
- `discovery` - Learning about the environment
- `lateral-movement` - Moving through networks
- `collection` - Gathering data of interest
- `exfiltration` - Stealing data
- `command-and-control` - Communicating with controlled systems
- `impact` - Disrupting or destroying systems
- `utilities` - General utility tools

## Plugin Development Best Practices

### 1. Code Structure

- Keep your code modular and well-organized
- Use clear function and variable names
- Include docstrings and comments
- Handle errors gracefully
- Provide informative error messages

### 2. Configuration

- Use the `configuration` field in `plugin.json` for default settings
- Allow users to override configuration
- Document all configuration options in your README

### 3. Dependencies

- Minimize external dependencies when possible
- Clearly document all dependencies
- Specify exact versions for critical dependencies
- Test with specified dependency versions

### 4. Security

- Never hardcode credentials or sensitive data
- Use environment variables for sensitive configuration
- Implement proper input validation
- Follow secure coding practices
- Include security warnings in documentation

### 5. Documentation

Your README.md should include:

- Clear description of what the plugin does
- Installation instructions
- Usage examples
- Configuration options
- Requirements
- Security notices
- License information

### 6. Testing

- Test your plugin on all supported platforms
- Include error handling tests
- Test with various input scenarios
- Verify compatibility with specified dependencies

## Example Plugin

See the `network-scanner` plugin for a complete example:

```python
#!/usr/bin/env python3
"""
Your Plugin Name
Description of what it does
"""

import json
import sys
from typing import Dict, Optional


class YourPlugin:
    """Main plugin class"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        # Initialize your plugin
    
    def main_function(self, args):
        """Main plugin functionality"""
        # Your code here
        pass


def main():
    """Entry point"""
    plugin = YourPlugin()
    
    if len(sys.argv) < 2:
        print("Usage: your-plugin.py <command> [options]")
        sys.exit(1)
    
    command = sys.argv[1]
    # Handle commands
    
    result = plugin.main_function(command)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

## Submitting Your Plugin

1. **Fork the repository** on GitHub
2. **Create your plugin** in the `plugins/` directory
3. **Update registry.json** to include your plugin
4. **Test thoroughly** on all supported platforms
5. **Create a pull request** with:
   - Plugin code and documentation
   - Updated registry.json
   - Description of what your plugin does
   - Test results

## Plugin Validation

Before submitting, ensure your plugin:

- [ ] Has a valid `plugin.json` that conforms to the schema
- [ ] Has comprehensive README.md documentation
- [ ] Includes a working entrypoint file
- [ ] Is tested on specified platforms
- [ ] Has no hardcoded credentials or sensitive data
- [ ] Includes proper error handling
- [ ] Has a valid open-source license
- [ ] Follows security best practices

## Getting Help

- Check existing plugins for examples
- Review the plugin schema: `plugin-schema.json`
- Open an issue on GitHub for questions
- Join the community discussions

## Legal and Ethical Guidelines

**IMPORTANT**: All plugins in this marketplace are intended for:

- Authorized security testing
- Educational purposes
- Legitimate red team exercises
- Penetration testing with proper authorization

Users and developers must:

- Obtain proper authorization before use
- Follow all applicable laws and regulations
- Use tools responsibly and ethically
- Not use for malicious purposes

Violation of these guidelines may result in plugin removal and legal consequences.
