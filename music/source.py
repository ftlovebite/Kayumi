import yt_dlp

from music.song import Song

YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "quiet": True,
    "default_search": "ytsearch",
    "extract_flat": False,
    "noplaylist": True,
}


class YTDLSource:

    def __init__(self):
        self.ytdl = yt_dlp.YoutubeDL(YTDL_OPTIONS)

    def search(self, query: str, requester: int):

        info = self.ytdl.extract_info(query, download=False)

        if "entries" in info:
            info = info["entries"][0]

        return Song(
            title=info.get("title", "Unknown"),
            webpage_url=info.get("webpage_url", ""),
            stream_url=info.get("url", ""),
            duration=info.get("duration", 0),
            thumbnail=info.get("thumbnail", ""),
            uploader=info.get("uploader", "Unknown"),
            requester=requester,
        )


source = YTDLSource()
