from music.queue import MusicQueue


class GuildPlayer:
    def __init__(self):
        self.queue = MusicQueue()

        self.voice_client = None

        self.current = None

        self.volume = 0.8

        self.is_playing = False

        self.text_channel = None

        self.now_playing_message = None


players = {}


def get_player(guild_id: int) -> GuildPlayer:
    if guild_id not in players:
        players[guild_id] = GuildPlayer()

    return players[guild_id]
