import pyglet

class Circuit:
    def __init__(self, type, x, y):
        self.type = type
        self.image = None
        self.positionX = x
        self.positionY = y
        self.selected = False
        setup(self)

        
    def draw(self):
        if self.type != '':
            self.image.blit(self.positionX, self.positionY)

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def setSelected(self, val):
        self.selected = val

    def getSelected(self):
        return self.selected

    def getType(self):
        return self.type

def setup(self):
    if self.type == 'and':
        self.image = pyglet.image.load("./images/and.png")
    elif self.type == 'or':
        self.image = pyglet.image.load("./images/or.png")
    elif self.type == '':
        pass
