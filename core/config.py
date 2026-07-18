import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)


def is_owner(user_id: int):
    return user_id in config.get("owners", [])
