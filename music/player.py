from music.queue import MusicQueue


class GuildPlayer:
    def __init__(self):
        self.queue = MusicQueue()
        self.voice_client = None
        self.current = None
        self.volume = 80


players = {}


def get_player(guild_id: int) -> GuildPlayer:
    if guild_id not in players:
        players[guild_id] = GuildPlayer()

    return players[guild_id]
