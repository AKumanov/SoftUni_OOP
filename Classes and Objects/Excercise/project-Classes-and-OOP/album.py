class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = []
        for x in songs:
            self.add_song(x)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                if not self.published:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
                return f"Cannot remove songs. Album is published."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = "\n".join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n" + album_info
