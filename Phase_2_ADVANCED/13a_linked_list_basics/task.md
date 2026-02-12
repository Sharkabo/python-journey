# Task Description

**Scenario: The Spotify Clone Playlist**

You are building the audio engine for a music streaming app. A standard Python list (`[]`) isn't ideal for a playlist because if a user is listening to Song A, the "next" song needs to be strictly linked to it. If you shuffle the playlist, you're just changing these links. You need a data structure where each song knows exactly which song comes next.

**Your Goal:**
Implement a **Singly Linked List** from scratch to represent a playlist of songs.

**Objectives:**
1.  Create a `SongNode` class. It should have `self.song_name` and `self.next_song` (default None).
2.  Create a `Playlist` class with `self.head`.
3.  Implement `add_song(name)`: Adds a new song to the *end* of the list. (You'll need to traverse from the head to find the last node).
4.  Implement `play_all()`: Traverses from the head, printing "Now playing: [Song Name]" until it reaches the end.

**Success Condition:**
Add 3 songs: "Shape of You", "Despacito", "Industry Baby".
Run `play_all()`. It should print them in the correct order.
Prove it's a linked list: Manually check that `playlist.head.next_song.song_name` gives you the second song!
