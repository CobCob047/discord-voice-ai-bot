# 🎙️ Discord Voice AI Bot

**Advanced open-source Discord voice assistant with real-time transcription, AI responses, and comprehensive analytics**

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GPU](https://img.shields.io/badge/GPU-NVIDIA%20Required-76b900.svg)](https://www.nvidia.com/)

## ✨ Features

- 🎙️ **Real-time voice transcription** using OpenAI Whisper Large-v3
- 🤖 **AI-powered responses** via Ollama (any LLM)
- 📊 **Advanced analytics** - user stats, leaderboards, conversation analysis
- 🎵 **Music playback** - YouTube, Spotify integration
- 🔒 **Privacy-focused** - fully self-hosted, encrypted database
- 200+ voice commands with wake word detection

## 🚀 Quick Start

### Prerequisites

- **NVIDIA GPU** (RTX 3060+ recommended, RTX 4090 ideal)
- Ubuntu 22.04/24.04
- Python 3.12+
- 16GB+ RAM

### Installation

See [INSTALLATION.md](INSTALLATION.md) for complete setup guide.

Quick start:
```bash
git clone https://github.com/CobCob047/discord-voice-ai-bot.git
cd discord-voice-ai-bot
pip install -r requirements.txt
python patch_opus.py
cp .env.example .env
# Edit .env with your Discord token
python bot.py
```

## 📖 Documentation

- [Installation Guide](INSTALLATION.md) - Complete setup instructions
- [Commands Reference](COMMANDS.md) - All 200+ voice commands
- [Configuration](CONFIGURATION.md) - Customization options

## 🏢 Managed Hosting

Don't have an RTX 4090? [OneRaap Hosting](https://discord.gg/mHsqykcyZa) offers managed hosting starting at $20/month.

## 📄 License

MIT License - see [LICENSE](LICENSE)

**Created by [Cob](https://github.com/CobCob047) / [OneRaap Hosting](https://oneraap.com)**
