from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import discord


@dataclass(slots=True)
class Song:
    """
    Represents a playable song in Kayumi.
    """

    title: str
    webpage_url: str
    stream_url: str

    duration: int = 0
    thumbnail: str = ""
    uploader: str = ""

    requester: Optional[discord.Member] = None

    is_live: bool = False

    source: str = "youtube"

    added_by: Optional[int] = None

    metadata: dict = field(default_factory=dict)

    @property
    def duration_string(self) -> str:
        """
        Converts seconds into HH:MM:SS
        """

        if self.is_live:
            return "LIVE"

        seconds = int(self.duration)

        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        if hours:
            return f"{hours:02}:{minutes:02}:{seconds:02}"

        return f"{minutes:02}:{seconds:02}"

    @property
    def requester_name(self) -> str:
        if self.requester:
            return self.requester.display_name
        return "Unknown"

    @property
    def requester_avatar(self) -> str:
        if self.requester:
            return self.requester.display_avatar.url
        return ""

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "webpage_url": self.webpage_url,
            "stream_url": self.stream_url,
            "duration": self.duration,
            "thumbnail": self.thumbnail,
            "uploader": self.uploader,
            "is_live": self.is_live,
            "source": self.source,
            "added_by": self.added_by,
        }

    @classmethod
    def from_yt_dlp(cls, data: dict, requester: Optional[discord.Member] = None):
        """
        Create Song from yt-dlp extracted info.
        """

        return cls(
            title=data.get("title", "Unknown Title"),
            webpage_url=data.get("webpage_url", data.get("original_url", "")),
            stream_url=data["url"],
            duration=data.get("duration") or 0,
            thumbnail=data.get("thumbnail", ""),
            uploader=data.get("uploader", ""),
            requester=requester,
            is_live=data.get("is_live", False),
            source="youtube",
            added_by=requester.id if requester else None,
            metadata=data,
        )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Song title='{self.title}'>"
