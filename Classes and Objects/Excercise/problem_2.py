class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        if self.hours == Time.max_hours and self.minutes == Time.max_minutes and self.seconds == Time.max_seconds:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.get_time()
        elif self.hours <= Time.max_hours and self.minutes <= Time.max_minutes and self.seconds < Time.max_seconds:
            self.seconds += 1
            self.get_time()

        elif self.hours < Time.max_hours and self.minutes == Time.max_minutes and self.seconds == Time.max_seconds:
            self.seconds = 0
            self.minutes = 0
            self.get_time()


time = Time(9, 30, 59)
print(time.get_time())
time.set_time(22, 59, 59)
print(time.get_time())
print(time.next_second())

