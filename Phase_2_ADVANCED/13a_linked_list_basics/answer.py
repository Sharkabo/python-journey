from __future__ import annotations
from typing import Any

class SongNode:
    def __init__(self, song_name: str) -> None:
        self.song_name = song_name
        self.next_song: SongNode | None = None

class Playlist:
    def __init__(self) -> None:
        self.head = None
    
    def add_song(self, data: Any)-> Any:
        new_song = SongNode(data)
        if not self.head:
            self.head = new_song
            return
        current = self.head
        while current.next_song:
            current = current.next_song
        current.next_song = new_song
    
    def play_all(self)-> Any:
        current = self.head
        if not current:
            print('The playlist is empty')
        print('Start the playlist')
        while current:
            print(f'{current.song_name}')
            current = current.next_song
        print('End of the playlist')