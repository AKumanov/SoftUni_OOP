class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()
                self.guests -= room.guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
