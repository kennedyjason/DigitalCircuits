import pyglet

# DigitalCircuits
#
# @author Jason Kennedy
# @version 1

class Part:
    #Constructor
    #
    #    type: is one of two values(for now): and, or
    #      id: is determined by the number of items in the parts list
    # 	       at the time the part is created
    #       x: the starting x position
    #       y: the starting y position
    #  inputs: the number of inputs
    # outputs: the number of outputs
    # deleted: a temporary solution to deleting parts
    def __init__(self, type, id, x, y):
        self.id = id
        self.type = type
        self.image = None
        self.positionX = x
        self.positionY = y
        self.selected = False
        self.inputs = 0
        self.outputs = 0
        self.button = False

        self.deleted = False

        #Right now this just determines the image
        setup(self)

    #Draw the image of the part to the screen
    # called during the on_draw() window.event
    def draw(self):
        if self.type != '':
            self.image.blit(self.positionX, self.positionY)

    #Set the position of part, eventually snap to grid?
    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    #Set the part to selected
    def setSelected(self, val):
        self.selected = val

    #Return if the part is selected
    def getSelected(self):
        return self.selected

    #Return the type of the part
    def getType(self):
        return self.type

    #Return the id of the part
    def getId(self):
        return self.id

    #Determine if the mouse was inside the part when clicked
    def mouseInside(self, x, y):
        if x > self.positionX and x < self.positionX + 100 and y > self.positionY and y < self.positionY + 50:
            return True
        return False

    #Remove part
    def removePart(self):
        self.deleted = True
    def getRemoved(self):
        return self.deleted

    #set the part to a button
    def setButton(self):
        self.button = True
    def getButton(self):
        return self.button

    #Updates the buttons image
    def update(self):
        if self.type == 'and':
            self.image = pyglet.image.load("./images/and.png")
        elif self.type == 'or':
            self.image = pyglet.image.load("./images/or.png")

#Set up the image of the parrt
def setup(self):
    if not self.button:
        #set up the image
        if self.type == 'and':
            self.image = pyglet.image.load("./images/andGate.png")
            self.inputs = 2
            self.outputs = 1
        elif self.type == 'or':
            self.image = pyglet.image.load("./images/orGate.png")
            self.inputs = 2
            self.outputs = 1
        elif self.type == '':
            pass
