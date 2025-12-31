#!/usr/bin/env python3
"""
Opus Codec Patch Script
Fixes discord-ext-voice-recv to handle corrupted audio packets gracefully
"""

import os
import sys
from pathlib import Path

def find_opus_file():
    """Locate the opus.py file in the installed packages"""
    possible_paths = [
        Path('venv/lib/python3.12/site-packages/discord/ext/voice_recv/opus.py'),
        Path('venv/lib/python3.11/site-packages/discord/ext/voice_recv/opus.py'),
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    try:
        import discord.ext.voice_recv
        package_path = Path(discord.ext.voice_recv.__file__).parent / 'opus.py'
        if package_path.exists():
            return package_path
    except ImportError:
        pass
    
    return None

def patch_opus():
    """Apply the patch to handle corrupted packets"""
    opus_file = find_opus_file()
    
    if not opus_file:
        print("❌ Could not locate opus.py file")
        print("Please ensure discord-ext-voice-recv is installed:")
        print("  pip install discord-ext-voice-recv")
        sys.exit(1)
    
    print(f"📁 Found opus.py at: {opus_file}")
    
    with open(opus_file, 'r') as f:
        content = f.read()
    
    if 'Skip corrupted packets' in content:
        print("✅ File is already patched!")
        return
    
    old_code = '''    def _decode_packet(self, packet: AudioPacket) -> Tuple[AudioPacket, bytes]:
        assert self._decoder is not None
        # Decode as per usual
        if packet:
            pcm = self._decoder.decode(packet.decrypted_data, fec=False)'''
    
    new_code = '''    def _decode_packet(self, packet: AudioPacket) -> Tuple[AudioPacket, bytes]:
        assert self._decoder is not None
        # Decode as per usual
        if packet:
            try:
                pcm = self._decoder.decode(packet.decrypted_data, fec=False)
            except Exception as e:
                # Skip corrupted packets, return silence
                return packet, bytes(3840)'''
    
    if old_code not in content:
        print("⚠️  Could not find expected code pattern")
        print(f"  File: {opus_file}")
        sys.exit(1)
    
    content = content.replace(old_code, new_code)
    
    with open(opus_file, 'w') as f:
        f.write(content)
    
    print("✅ Successfully patched opus.py!")
    print("\nThe bot can now handle corrupted audio packets from:")
    print("  • Mobile Discord users")
    print("  • Poor network conditions")
    print("  • Discord voice server issues")

if __name__ == '__main__':
    print("=" * 60)
    print("Discord Voice AI Bot - Opus Codec Patcher")
    print("=" * 60)
    print()
    patch_opus()
