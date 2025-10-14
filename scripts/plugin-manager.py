#!/usr/bin/env python3
"""
Super Rouge Hunter Marketplace Plugin Manager
Install, update, and manage plugins from the marketplace
"""

import json
import os
import shutil
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class PluginManager:
    """Manage plugins from the marketplace"""
    
    def __init__(self, marketplace_dir: Optional[str] = None):
        if marketplace_dir:
            self.marketplace_dir = Path(marketplace_dir)
        else:
            self.marketplace_dir = Path(__file__).parent.parent
        
        self.registry_file = self.marketplace_dir / "registry.json"
        self.plugins_dir = self.marketplace_dir / "plugins"
        self.installed_file = Path.home() / ".super-rouge-hunter" / "installed.json"
        
        # Ensure directories exist
        self.installed_file.parent.mkdir(parents=True, exist_ok=True)
        
    def load_registry(self) -> Dict:
        """Load the plugin registry"""
        try:
            with open(self.registry_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Registry file not found at {self.registry_file}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Registry file contains invalid JSON: {e}")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied reading {self.registry_file}")
            sys.exit(1)
    
    def load_installed(self) -> Dict:
        """Load installed plugins list"""
        if self.installed_file.exists():
            try:
                with open(self.installed_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Warning: Installed plugins file contains invalid JSON: {e}")
                print("Creating new installed plugins list...")
                return {"plugins": []}
            except PermissionError:
                print(f"Error: Permission denied reading {self.installed_file}")
                sys.exit(1)
        return {"plugins": []}
    
    def save_installed(self, data: Dict):
        """Save installed plugins list"""
        try:
            with open(self.installed_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error: Failed to save installed plugins: {e}")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied writing to {self.installed_file}")
            sys.exit(1)
        except OSError as e:
            print(f"Error: System error while saving: {e}")
            sys.exit(1)
    
    def list_available(self, category: Optional[str] = None):
        """List available plugins"""
        registry = self.load_registry()
        plugins = registry.get("plugins", [])
        
        if category:
            plugins = [p for p in plugins if p.get("category") == category]
        
        print(f"\n{'ID':<30} {'Name':<30} {'Category':<20} {'Version'}")
        print("-" * 100)
        
        for plugin in plugins:
            print(f"{plugin['id']:<30} {plugin['name']:<30} {plugin['category']:<20} {plugin['version']}")
        
        print(f"\nTotal: {len(plugins)} plugins")
    
    def list_installed(self):
        """List installed plugins"""
        installed = self.load_installed()
        plugins = installed.get("plugins", [])
        
        if not plugins:
            print("No plugins installed.")
            return
        
        print(f"\n{'ID':<30} {'Name':<30} {'Version':<15} {'Status'}")
        print("-" * 100)
        
        for plugin in plugins:
            print(f"{plugin['id']:<30} {plugin['name']:<30} {plugin['version']:<15} {plugin.get('status', 'active')}")
        
        print(f"\nTotal: {len(plugins)} plugins installed")
    
    def search(self, query: str):
        """Search for plugins"""
        registry = self.load_registry()
        plugins = registry.get("plugins", [])
        
        results = []
        query_lower = query.lower()
        
        for plugin in plugins:
            if (query_lower in plugin['id'].lower() or
                query_lower in plugin['name'].lower() or
                query_lower in plugin['description'].lower() or
                any(query_lower in tag.lower() for tag in plugin.get('tags', []))):
                results.append(plugin)
        
        if not results:
            print(f"No plugins found matching '{query}'")
            return
        
        print(f"\nFound {len(results)} plugin(s) matching '{query}':\n")
        print(f"{'ID':<30} {'Name':<30} {'Description'}")
        print("-" * 100)
        
        for plugin in results:
            desc = plugin['description'][:40] + "..." if len(plugin['description']) > 40 else plugin['description']
            print(f"{plugin['id']:<30} {plugin['name']:<30} {desc}")
    
    def show_info(self, plugin_id: str):
        """Show detailed information about a plugin"""
        registry = self.load_registry()
        plugins = registry.get("plugins", [])
        
        plugin = next((p for p in plugins if p['id'] == plugin_id), None)
        
        if not plugin:
            print(f"Plugin '{plugin_id}' not found in marketplace.")
            return
        
        print(f"\n{'='*60}")
        print(f"Plugin: {plugin['name']}")
        print(f"{'='*60}")
        print(f"ID:          {plugin['id']}")
        print(f"Version:     {plugin['version']}")
        print(f"Author:      {plugin['author']}")
        print(f"Category:    {plugin['category']}")
        print(f"License:     {plugin.get('license', 'N/A')}")
        print(f"Repository:  {plugin.get('repository', 'N/A')}")
        print(f"\nDescription:")
        print(f"  {plugin['description']}")
        
        if plugin.get('tags'):
            print(f"\nTags: {', '.join(plugin['tags'])}")
        
        if plugin.get('compatibility'):
            compat = plugin['compatibility']
            print(f"\nCompatibility:")
            if compat.get('platforms'):
                print(f"  Platforms: {', '.join(compat['platforms'])}")
            if compat.get('minVersion'):
                print(f"  Min Version: {compat['minVersion']}")
        
        print()
    
    def install(self, plugin_id: str):
        """Install a plugin"""
        registry = self.load_registry()
        plugins = registry.get("plugins", [])
        
        plugin = next((p for p in plugins if p['id'] == plugin_id), None)
        
        if not plugin:
            print(f"Error: Plugin '{plugin_id}' not found in marketplace.")
            return False
        
        # Check if already installed
        installed = self.load_installed()
        if any(p['id'] == plugin_id for p in installed.get("plugins", [])):
            print(f"Plugin '{plugin_id}' is already installed.")
            return False
        
        print(f"Installing {plugin['name']} v{plugin['version']}...")
        
        # In a real implementation, this would copy or download the plugin
        source_path = self.plugins_dir / plugin_id
        if not source_path.exists():
            print(f"Warning: Plugin source not found at {source_path}")
        
        # Add to installed list
        installed['plugins'].append({
            'id': plugin['id'],
            'name': plugin['name'],
            'version': plugin['version'],
            'status': 'active',
            'installed_at': datetime.now().astimezone().isoformat()
        })
        
        self.save_installed(installed)
        print(f"Successfully installed {plugin['name']}!")
        return True
    
    def uninstall(self, plugin_id: str):
        """Uninstall a plugin"""
        installed = self.load_installed()
        plugins = installed.get("plugins", [])
        
        plugin = next((p for p in plugins if p['id'] == plugin_id), None)
        
        if not plugin:
            print(f"Plugin '{plugin_id}' is not installed.")
            return False
        
        print(f"Uninstalling {plugin['name']}...")
        
        # Remove from installed list
        installed['plugins'] = [p for p in plugins if p['id'] != plugin_id]
        self.save_installed(installed)
        
        print(f"Successfully uninstalled {plugin['name']}!")
        return True


def main():
    """Main entry point"""
    manager = PluginManager()
    
    if len(sys.argv) < 2:
        print("Super Rouge Hunter Plugin Manager")
        print("\nUsage: plugin-manager.py <command> [options]")
        print("\nCommands:")
        print("  list [category]       - List available plugins")
        print("  installed             - List installed plugins")
        print("  search <query>        - Search for plugins")
        print("  info <plugin-id>      - Show plugin information")
        print("  install <plugin-id>   - Install a plugin")
        print("  uninstall <plugin-id> - Uninstall a plugin")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        manager.list_available(category)
    elif command == "installed":
        manager.list_installed()
    elif command == "search":
        if len(sys.argv) < 3:
            print("Error: search query required")
            sys.exit(1)
        manager.search(sys.argv[2])
    elif command == "info":
        if len(sys.argv) < 3:
            print("Error: plugin ID required")
            sys.exit(1)
        manager.show_info(sys.argv[2])
    elif command == "install":
        if len(sys.argv) < 3:
            print("Error: plugin ID required")
            sys.exit(1)
        manager.install(sys.argv[2])
    elif command == "uninstall":
        if len(sys.argv) < 3:
            print("Error: plugin ID required")
            sys.exit(1)
        manager.uninstall(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
