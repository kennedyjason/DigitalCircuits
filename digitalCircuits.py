import pyglet
from pyglet.window import mouse
from part import Part

def main():
    parts = []

    # Path to an image
    #path = '/home/wastedatoms/github/DigitalParts/images/and.png'
    label = pyglet.text.Label('-')

    #instantiate part as button
    AND = Part('and', 1, 0, 400)
    OR = Part('or', 2, 0, 350)

    #throwaway part for starting select
    defaultSelected = Part('and', 0, 0, 0)
    defaultSelected.setSelected(True)
    
    parts.append(defaultSelected)
    parts.append(AND)
    parts.append(OR)

    # Set up the window
    window = pyglet.window.Window()


    #
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:

            #clicked a create button
            if x > 0 and x < 101 and y > 400 and y < 450:#AND
                partCreate('and')
            elif x > 0 and x < 101 and y > 350 and y < 401:#OR
                partCreate('or')


            #clicked anywhere else
            #
            #check if inside a part if so, select it
            elif 1:
                counter = 0
                for p in parts:
                    if p.mouseInside(x,y):
                        findSelected().setSelected(False)
                        p.setSelected(True)
                        counter += 1
                if findSelected().getId() != 0 and counter == 0:#check is not default and that we didn't just select it
                    findSelected().setSelected(False)
                    defaultSelected.setSelected(True)


    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            findSelected().setPosition(x-50, y-25)#include offset so the mouse is centered on the part
            

    #create a part
    def partCreate(type):
        parts.append(Part(type, len(parts), 100, 100))

    def findSelected():
        for p in parts:
            if p.getSelected():
                return p
        print("None selescted")

    # Set up a label
    #label = pyglet.text.Label('Hello World!')

    # Set up an image
    #image = pyglet.image.load(path)

    # idk
    @window.event
    def on_draw():
        window.clear()
        label.draw()
        for p in parts:
            if p.getId() > 0:
                p.draw()
    run()

# start the application
def run():
    pyglet.app.run()

# idk
if __name__ == '__main__':
    main()

