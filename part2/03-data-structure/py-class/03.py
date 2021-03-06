class Point():
    d = {
        'n': (0, 1),
        'ne': (1, 1),
        'e': (1, 0),
        'se': (1, -1),
        's': (0, -1)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x = {self.x}; y = {self.y}'
    
    def move(self, direct):
        self.x += self.d[direct][0]
        self.y += self.d[direct][1]


a = Point(10,3)

print(a)
a.move('ne')
print(a)
