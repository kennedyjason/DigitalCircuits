import pyglet
from pyglet.window import mouse
from part import Part

# DigitalCircuits
#
# @author Jason Kennedy
# @version 1

def main():

    # list of parts
    parts = []

    #instantiate part as button
    AND = Part('and', 1, 0, 400)
    OR = Part('or', 2, 0, 350)

    #throwaway part for starting select
    defaultSelected = Part('and', 0, 0, 0)
    defaultSelected.setSelected(True)

    #adding default parts to the list
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
                counter = 0# to insure we do not deselect if we just selected
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
    # parts is a list of parts, len(parts) is passed into the constructor of parts
    # to be used as the id of the created part
    # 100, 100 is just the default position of new parts
    def partCreate(type):
        parts.append(Part(type, len(parts), 100, 100))

    #findSelected
    # loops parts and check if a part is selected
    def findSelected():
        for p in parts:
            if p.getSelected():
                return p
        print("None selected")

    #
    @window.event
    def on_draw():
        window.clear()
        for p in parts:
            if p.getId() > 0:# > 0 so that we do not check the default selected part
                p.draw()
    run()

# start the application
def run():
    pyglet.app.run()

# idk
if __name__ == '__main__':
    main()

