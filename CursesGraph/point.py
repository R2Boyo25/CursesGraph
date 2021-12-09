class Point:
    def __init__(self, x = 0, y = 0, color = 0):
        self.x = x
        self.y = y
        self.color = color
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __gt__(self, o):
        return self.y > o.y