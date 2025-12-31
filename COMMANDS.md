# Voice Commands Reference

All commands start with your configured wake word (default: "Jarvis" or "Hey Jarvis")

## 📊 Statistics & Analytics

| Command | Description |
|---------|-------------|
| `who talks the most?` | Shows top 10 most active users |
| `top words` | Most frequently used words |
| `top swear words` | Profanity leaderboard |
| `my stats` | Your personal statistics |
| `[user]'s stats` | Stats for specific user |
| `who talked the most yesterday?` | Yesterday's top talker |
| `who talked the most last week?` | Last week's top talker |
| `show me stats from [date]` | Custom date range stats |
| `conversation topics` | AI-analyzed conversation themes |

## 🤖 AI Questions & Information

| Command | Description |
|---------|-------------|
| `what's the weather in [city]?` | Current weather |
| `search for [query]` | Web search with DuckDuckGo |
| `explain [topic]` | Detailed explanations |
| `who is [person]?` | Biographical information |
| `what is [thing]?` | Definitions and context |
| `[any question]` | General AI conversation |

## 🎵 Music Control

### Playback
| Command | Description |
|---------|-------------|
| `play [song/artist]` | Play music from YouTube/Spotify |
| `pause` | Pause current track |
| `resume` | Resume playback |
| `skip` | Skip to next song |
| `stop` | Stop music and clear queue |
| `volume [0-100]` | Adjust volume |

### Queue Management
| Command | Description |
|---------|-------------|
| `queue` | Show current queue |
| `shuffle` | Shuffle the queue |
| `clear queue` | Remove all queued songs |
| `remove [number]` | Remove song from queue |

### Advanced
| Command | Description |
|---------|-------------|
| `enable auto DJ` | AI-powered music selection |
| `disable auto DJ` | Turn off auto DJ |
| `loop` | Enable loop mode |
| `now playing` | Show current track info |

## 🎮 Fun & Games

| Command | Description |
|---------|-------------|
| `tell me a joke` | Random joke |
| `flip a coin` | Heads or tails |
| `roll a dice` | Random number 1-6 |
| `roll [X]d[Y]` | Roll X dice with Y sides (e.g., "roll 2d20") |
| `pick [option1] or [option2]` | Random choice |
| `compliment me` | Get a compliment |
| `roast [user]` | Playful roast |

## 👥 User Interaction

| Command | Description |
|---------|-------------|
| `who's in voice?` | List current voice channel members |
| `how long has [user] been here?` | Time in voice channel |
| `kick [user]` | Kick user from voice (requires permissions) |
| `mute [user]` | Server mute user |
| `unmute [user]` | Server unmute user |

## 🔧 Bot Management

| Command | Description |
|---------|-------------|
| `join voice` | Join your current voice channel |
| `leave voice` | Leave voice channel |
| `clear chat` | Clear bot messages (requires permissions) |
| `help` | Show available commands |
| `version` | Bot version information |
| `uptime` | How long bot has been running |
| `ping` | Check bot latency |

## 🎤 Voice & Transcription

| Command | Description |
|---------|-------------|
| `enable transcription` | Start logging voice to text |
| `disable transcription` | Stop transcription |
| `read transcription` | Read recent transcriptions aloud |
| `export transcription` | Export logs to file |

## 💬 Conversation

| Command | Description |
|---------|-------------|
| `remember [fact]` | Store information for later |
| `what do you remember about [topic]?` | Recall stored information |
| `forget [topic]` | Delete stored information |
| `summarize the last [X] minutes` | AI conversation summary |

## 📈 Advanced Analytics

| Command | Description |
|---------|-------------|
| `conversation analysis` | Deep analysis of chat patterns |
| `relationship map` | Who talks to whom most |
| `top topics today` | AI-identified discussion topics |
| `sentiment analysis` | Conversation mood/tone |
| `export all stats` | Download complete analytics |

## 🎭 Personality & Customization

| Command | Description |
|---------|-------------|
| `change personality to [style]` | Adjust AI behavior |
| `speak like [character]` | Roleplay mode |
| `formal mode` | Professional responses |
| `casual mode` | Relaxed conversation |

## 🔒 Admin Commands

(Requires administrator permissions)

| Command | Description |
|---------|-------------|
| `reset database` | Clear all stored data |
| `backup database` | Create database backup |
| `reload config` | Reload configuration |
| `update model` | Switch Ollama model |
| `enable debug mode` | Verbose logging |
| `disable debug mode` | Normal logging |

---

## Custom Wake Words

You can configure custom wake words in `.env`:

```env
WAKE_WORDS=jarvis,hey jarvis,computer,friday
```

All commands will then respond to any of these phrases.

---

## Voice Command Tips

1. **Speak clearly** - Whisper works best with distinct speech
2. **Use the wake word** - Always start with "Jarvis" (or your custom wake word)
3. **Natural language** - You don't need exact phrasing, the AI understands context
4. **Mobile users** - May experience slight transcription delays due to network
5. **Background noise** - The bot filters most noise automatically

---

## Command Aliases

Many commands have multiple ways to invoke them:

- "play music" = "play song" = "start music"
- "who talks most" = "who talks the most" = "top talker"
- "tell joke" = "tell me a joke" = "say something funny"
- "weather" = "what's the weather" = "check weather"

The AI understands variations!
