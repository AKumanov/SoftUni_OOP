from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for x in self.albums:
            if x.name == album_name:
                if x.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(x)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        band_details = "\n".join(f"{alb.details()}" for alb in self.albums)
        return f"Band {self.name}\n" + band_details


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
