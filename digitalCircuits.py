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
    # list of button
    buttons = []
    
    #instantiate part as button
    AND = Part('and', 0, 5, 545)
    OR = Part('or', 1, 5, 490)

    AND.setButton()
    OR.setButton()

    #throwaway part for starting select
    defaultSelected = Part('and', 0, 0, 0)
    defaultSelected.setSelected(True)

    #adding default parts to the list
    parts.append(defaultSelected)
    buttons.append(AND)
    buttons.append(OR)

    # Set up the window
    WIDTH = 1200
    HEIGHT = 600
    window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
    bgImage = pyglet.image.SolidColorImagePattern((100,100,100,255)).create_image(WIDTH, HEIGHT)
    buttonLine = pyglet.image.SolidColorImagePattern((0,0,0,255)).create_image(2, HEIGHT)

    #
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:

            #clicked a create button
            if x > 5 and x < 106 and y > 545 and y < 595:#AND
                partCreate('and')
            elif x > 5 and x < 106 and y > 485 and y < 535:#OR
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


        #Right Click            
        elif button == mouse.RIGHT:

            #clicked a part
            #
            # remove the clicked part
            for p in parts:
                if p.mouseInside(x, y) and not p.getButton():
                    p.removePart()





            

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            findSelected().setPosition(x-50, y-25)#include offset so the mouse is centered on the part
            

    #create a part
    # parts is a list of parts, len(parts) is passed into the constructor of parts
    # to be used as the id of the created part
    # 100, 100 is just the default position of new parts
    def partCreate(type):
        parts.append(Part(type, len(parts), 120, 545))# 10 pixels left of the AND button

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
        bgImage.blit(0,0)
        buttonLine.blit(110, 0)#5 pixels to the right of the buttons
        #draw buttons
        for b in buttons:
            b.update()#update button image
            b.draw()
        
        #draw parts
        for p in parts:
            if p.getId() > 0 and not p.getRemoved():# > 0 so that we do not check the default selected and deleted part
                p.draw()
    run()

# start the application
def run():
    pyglet.app.run()

# idk
if __name__ == '__main__':
    main()

