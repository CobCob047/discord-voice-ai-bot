<div align="center">

# 🎙️ Discord Voice AI Bot

### The most advanced open-source Discord voice assistant

Real-time transcription • AI responses • User analytics • Music playback • 200+ voice commands

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GPU](https://img.shields.io/badge/GPU-NVIDIA%20Required-76b900.svg)](https://www.nvidia.com/)

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Commands](#-voice-commands) • [Hosting](#-managed-hosting)

---

</div>

## ✨ Features

### 🎙️ Voice Recognition & Transcription
- **Real-time speech-to-text** using OpenAI Whisper (Large-v3)
- **Emotion detection** from voice tone and pitch analysis
- **Voice biometrics** - unique audio profile for each user
- **Multi-language support** - transcribe in 50+ languages
- **Mobile-friendly** - handles poor network conditions gracefully

### 🤖 AI-Powered Responses
- **Ollama integration** - Run any local LLM (Llama, Mistral, Dolphin-Mixtral, etc.)
- **Context-aware** - Remembers conversation history
- **Web search capability** - Answers current questions with DuckDuckGo
- **Customizable personality** - Easy to modify AI behavior

### 📊 Advanced Analytics
- **User leaderboards** - Who talks most, top words, profanity tracking
- **Conversation analysis** - Topics, relationships, speaking patterns
- **Time-based filters** - Stats for today, yesterday, this week, custom ranges
- **Voice activity tracking** - Complete history with SQLite database
- **Behavioral pattern analysis** - Social dynamics, engagement metrics

### 🎵 Music & Entertainment
- **YouTube playback** - High-quality audio streaming
- **Spotify integration** - Search and play from Spotify
- **Auto DJ mode** - AI-powered music selection based on conversation energy
- **Queue management** - Skip, pause, shuffle, volume control
- **Soundboard** - Custom audio clips

### 🛠️ Advanced Features
- **200+ voice commands** - Wake word detection ("Hey Jarvis")
- **Multi-server support** - Run on unlimited Discord servers
- **Per-server logging** - Each server gets isolated transcription logs
- **Voice cloning** - TTS with user voice samples (optional)
- **Database encryption** - Secure conversation storage with SQLCipher

---

## 🚀 Quick Start

### Prerequisites

**Hardware Requirements:**
- **NVIDIA GPU** (Required for real-time transcription)
  - Minimum: RTX 3060 (12GB VRAM)
  - Recommended: RTX 4090 (24GB VRAM)
  - Why: Whisper Large-v3 needs GPU acceleration for real-time performance
- **16GB+ System RAM**
- **50GB+ Storage** (for models and transcription logs)

**Software Requirements:**
- Ubuntu 22.04/24.04 (or compatible Linux)
- Python 3.12+
- NVIDIA CUDA drivers installed
- FFmpeg

### 1️⃣ Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** → Give it a name → **Create**
3. Go to **Bot** tab → Click **Add Bot** → **Yes, do it!**
4. Under **Privileged Gateway Intents**, enable:
   - ✅ Presence Intent
   - ✅ Server Members Intent  
   - ✅ Message Content Intent
5. Click **Reset Token** → Copy your bot token (save this securely!)
6. Go to **OAuth2** → **URL Generator**
   - Scopes: ✅ `bot` ✅ `applications.commands`
   - Bot Permissions: ✅ Administrator (or manually select: Read Messages, Send Messages, Connect, Speak, Use Voice Activity)
7. Copy the generated URL and open it in browser to invite bot to your server

---

## 📦 Installation

### Step 1: System Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y git python3.12 python3-pip python3-venv ffmpeg

# Install Opus codec (CRITICAL - prevents voice crashes)
sudo apt install -y libopus0 libopus-dev

# Verify installation
dpkg -l | grep opus
# Should show both libopus0 and libopus-dev
```

### Step 2: Install Ollama (AI Backend)
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve > /dev/null 2>&1 &

# Pull AI model (choose one - or try multiple!)
ollama pull dolphin-mixtral:8x7b    # Recommended: Fast, uncensored, 8x7B model
# OR
ollama pull llama3.1:8b             # Alternative: Meta's Llama 3.1
# OR  
ollama pull qwen2.5:7b              # Alternative: Qwen 2.5

# Verify model is ready
ollama list
# Should show your downloaded model
```

**Model Selection Guide:**
- `dolphin-mixtral:8x7b` - Best balance of speed/intelligence (recommended)
- `llama3.1:8b` - Fastest responses, good for casual use
- `qwen2.5:7b` - Excellent for technical questions
- `gemma2:27b` - Most intelligent but slower (needs 24GB VRAM)

### Step 3: Clone Repository
```bash
# Clone the repo
git clone https://github.com/CobCob047/discord-voice-ai-bot.git
cd discord-voice-ai-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Python Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

**What gets installed:**
- `py-cord` - Discord API library (maintained fork of discord.py)
- `discord-ext-voice-recv` - Voice recording capabilities
- `faster-whisper` - GPU-accelerated speech recognition
- `torch`, `torchaudio` - PyTorch for neural networks
- `librosa`, `soundfile` - Audio processing
- `httpx` - HTTP client for Ollama API
- `duckduckgo-search` - Web search integration
- `yt-dlp` - YouTube audio extraction
- `spotipy` - Spotify API (optional)
- `sqlcipher3` - Encrypted database
- `gtts` - Text-to-speech
- And more...

### Step 5: Fix Opus Codec Issues (CRITICAL)

Discord's voice library can crash with corrupted audio packets (especially from mobile users). This patches the library to handle errors gracefully:
```bash
# Run the automated patch script
python patch_opus.py
```

**What this does:**
- Locates `discord/ext/voice_recv/opus.py` in your Python environment
- Wraps the audio decoder in try/except to catch corrupted packets
- Returns silence instead of crashing when bad packets arrive
- Prevents the bot from disconnecting due to mobile Discord users

**Manual patch** (if script fails):
1. Find: `/path/to/venv/lib/python3.12/site-packages/discord/ext/voice_recv/opus.py`
2. Locate the `_decode_packet` method (around line 154)
3. Wrap the decoder call:
```python
def _decode_packet(self, packet: AudioPacket) -> Tuple[AudioPacket, bytes]:
    assert self._decoder is not None
    if packet:
        try:
            pcm = self._decoder.decode(packet.decrypted_data, fec=False)
            return packet, pcm
        except Exception as e:
            # Skip corrupted packets, return silence
            return packet, bytes(3840)
```

### Step 6: Configure Bot
```bash
# Copy example environment file
cp .env.example .env

# Edit with your credentials
nano .env
```

**Required settings** (`.env` file):
```env
# Discord Bot Token (from Step 1)
DISCORD_TOKEN=your_bot_token_here

# Ollama Configuration
OLLAMA_MODEL=dolphin-mixtral:8x7b
OLLAMA_URL=http://localhost:11434

# Optional: Spotify Integration
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

# Optional: Database Encryption (auto-generates if blank)
DB_PASSWORD=
```

### Step 7: Run the Bot
```bash
# Make sure Ollama is running
ollama serve > /dev/null 2>&1 &

# Start the bot
python bot.py

# Or run in background with logs
nohup python bot.py > bot.log 2>&1 &
```

**Expected output:**
```
Using device: cuda
Loading Whisper model...
Whisper model loaded!
Ollama model: dolphin-mixtral:8x7b
Bot is ready!
Connected to Discord servers: YourServerName
```

---

## 🎙️ Voice Commands

The bot listens for commands starting with **"Hey Jarvis"** or **"Jarvis"** (customizable).

### 📊 Stats & Analytics
```
"Jarvis, who talks the most?"
"Jarvis, top swear words"
"Jarvis, my stats"  
"Jarvis, who talked the most yesterday?"
"Jarvis, show me stats from last week"
"Jarvis, what are the top 10 words today?"
```

### 🤖 AI Questions
```
"Jarvis, what's the weather in Phoenix?"
"Jarvis, explain quantum computing"
"Jarvis, search for Discord API documentation"
"Jarvis, who won the 2024 election?"
```

### 🎵 Music
```
"Jarvis, play Bohemian Rhapsody"
"Jarvis, skip"
"Jarvis, pause"
"Jarvis, resume"
"Jarvis, enable auto DJ"
"Jarvis, volume 50"
```

**Full command list:** Over 200 commands available - see [COMMANDS.md](COMMANDS.md)

---

## ⚙️ Configuration

### Customizing the Bot Name

Edit `bot.py` and change the wake words:
```python
WAKE_WORDS = ["jarvis", "hey jarvis", "yo jarvis"]
BOT_NAME = "Jarvis"  # Used in responses
```

Now the bot responds to your custom name!

### Adjusting Whisper Model

Trade accuracy for speed by changing models in `bot.py`:
```python
# Options: tiny, base, small, medium, large-v3
whisper_model = WhisperModel("large-v3", device="cuda", compute_type="float16")
```

**Model comparison:**
- `tiny` - Fastest (1GB VRAM, 50% accuracy)
- `small` - Fast (2GB VRAM, 70% accuracy)
- `medium` - Balanced (5GB VRAM, 85% accuracy) 
- `large-v3` - **Best** (10GB VRAM, 95% accuracy) ← Recommended

---

## 🏢 Managed Hosting

**Don't have an RTX 4090?** Let us handle it for you.

[**OneRaap Hosting**](https://www.oneraap.com/gpu/) offers fully managed Discord voice AI bot hosting with RTX 4090 infrastructure.

✅ RTX 4090 GPU infrastructure  
✅ 99.9% uptime guarantee  
✅ Full setup & configuration included  
✅ Discord support  
✅ Custom voice commands  
✅ Automatic updates  


---

## 🛠️ Troubleshooting

### Bot crashes with OpusError

**Symptom:** `discord.opus.OpusError: corrupted stream`

**Solution:** Run the Opus patch script (Step 5 of installation). If already patched, verify:
```bash
dpkg -l | grep opus
# Should show both libopus0 and libopus-dev
```

### Ollama connection refused

**Symptom:** `Could not connect to Ollama server`

**Solution:**
```bash
# Start Ollama manually
ollama serve &

# Verify it's running
curl http://localhost:11434/api/tags
```

### Whisper model not loading

**Symptom:** `Failed to load Whisper model`

**Solution:** Check CUDA installation:
```bash
python -c "import torch; print(torch.cuda.is_available())"
# Should print: True

nvidia-smi  # Verify GPU is detected
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Credits

**Created by [Cob](https://github.com/CobCob047) / [OneRaap Hosting](https://www.oneraap.com)**

Built with:
- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition
- [Ollama](https://ollama.ai/) - Local LLM inference
- [py-cord](https://github.com/Pycord-Development/pycord) - Discord API
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) - Optimized Whisper
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube audio extraction

---

<div align="center">

**[⬆ Back to Top](#-discord-voice-ai-bot)**

Made with ❤️ by the OneRaap Hosting team

</div>
