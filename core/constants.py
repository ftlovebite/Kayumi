"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kayumi Premium Music Bot
Core Constants
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from typing import Final

# ==========================================================
# BOT
# ==========================================================

BOT_NAME: Final = "Kayumi"

BOT_VERSION: Final = "0.0.1 Alpha"

DEFAULT_PREFIX: Final = "!"

DEFAULT_VOLUME: Final = 80

MAX_QUEUE_SIZE: Final = 1000

AUTO_DISCONNECT: Final = 300


# ==========================================================
# EMBED COLORS
# ==========================================================

PURPLE = 0x8B5CF6
PINK = 0xEC4899
BLUE = 0x3B82F6
GREEN = 0x22C55E
RED = 0xEF4444
YELLOW = 0xFACC15
WHITE = 0xFFFFFF

DEFAULT_COLOR = PURPLE


# ==========================================================
# EMOJIS
# ==========================================================

PLAY = "▶️"
PAUSE = "⏸️"
STOP = "⏹️"
SKIP = "⏭️"
PREVIOUS = "⏮️"
SHUFFLE = "🔀"
LOOP = "🔁"
QUEUE = "📜"
SEARCH = "🔎"
VOLUME = "🔊"
MUSIC = "🎵"
HEART = "❤️"
SUCCESS = "✅"
ERROR = "❌"
WARNING = "⚠️"
LOADING = "⌛"


# ==========================================================
# FFMPEG
# ==========================================================

FFMPEG_OPTIONS = {
    "before_options":
        "-reconnect 1 "
        "-reconnect_streamed 1 "
        "-reconnect_delay_max 5",

    "options":
        "-vn"
}


# ==========================================================
# YT-DLP
# ==========================================================

YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "quiet": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "default_search": "ytsearch",
    "source_address": "0.0.0.0",
    "extract_flat": False,
}


# ==========================================================
# PLAYER
# ==========================================================

SEEK_STEP = 10

VOLUME_STEP = 10

MAX_VOLUME = 200

MIN_VOLUME = 0
