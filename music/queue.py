from collections import deque


class MusicQueue:
    def __init__(self):
        self.queue = deque()
        self.history = []
        self.loop = False

    def add(self, song):
        self.queue.append(song)

    def next(self):
        if not self.queue:
            return None

        song = self.queue.popleft()
        self.history.append(song)

        if self.loop:
            self.queue.append(song)

        return song

    def clear(self):
        self.queue.clear()

    def shuffle(self):
        import random

        songs = list(self.queue)
        random.shuffle(songs)

        self.queue = deque(songs)

    def previous(self):
        if not self.history:
            return None

        return self.history.pop()

    def __len__(self):
        return len(self.queue)
