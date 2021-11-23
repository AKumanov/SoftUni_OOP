class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.vowels_string = 'AEYUIOaeyuio'
        self.final = [el for el in self.text if el in self.vowels_string]
        self.end = len(self.final) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.final[index]


my_string = vowels('Abceio0oyuhg')
for char in my_string:
    print(char)
