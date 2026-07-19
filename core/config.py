import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


class Config:
    def __init__(self):
        self.reload()

    def reload(self):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.token = data.get("token", "")
        self.prefix = data.get("prefix", "!")
        self.owners = set(data.get("owners", []))
        self.default_volume = data.get("default_volume", 80)
        self.theme = data.get("theme", "purple")

    def is_owner(self, user_id: int) -> bool:
        return user_id in self.owners


config = Config()
