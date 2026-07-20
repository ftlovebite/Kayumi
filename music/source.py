import asyncio
import yt_dlp

from music.song import Song

YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "quiet": True,
    "default_search": "ytsearch",
    "noplaylist": True,
    "extract_flat": False,
}


class YTDLSource:

    def __init__(self):
        self.ytdl = yt_dlp.YoutubeDL(YTDL_OPTIONS)

    async def search(self, query: str, requester: int):

        loop = asyncio.get_running_loop()

        info = await loop.run_in_executor(
            None,
            lambda: self.ytdl.extract_info(query, download=False)
        )

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
