class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[''] * 4] * self.pages

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count)

    def add_photo(self, label: str):
        for row in range(len(self.photos[0])):
            for col in range(len(self.photos[row])):
                if not self.photos[row][col]:
                    self.photos[row][col] = '[]'
                    return f"{label} photo added successfully to page {row + 1} slot {col + 1}"
        return f"No more free slots"

    def display(self):
        final = ''
        separator = '-' * 9
        for row in range(len(self.photos)):
            final += separator
            final += ' \n'
            final += ''.join(self.photos[row])
            final += '\n'
        return final


album = PhotoAlbum(2)
print(album.add_photo('baby'))
print(album.photos)
print(album.add_photo('car'))
print(album.display())
