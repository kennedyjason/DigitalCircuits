import pyglet
from pyglet.window import mouse
from circuit import Circuit

def main():

    # Path to an image
    #path = '/home/wastedatoms/github/DigitalCircuits/images/and.png'
    label = pyglet.text.Label('-')
    #instantiate a circuit
    AND = Circuit('and', 100, 100)
    OR = Circuit('or', 400, 100)

    OR.setSelected(True)
    
    # Set up the window
    window = pyglet.window.Window()


    #
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.RIGHT:
            if OR.getSelected():
                OR.setSelected(False)
                AND.setSelected(True)
                print("AND")
            elif AND.getSelected():
                AND.setSelected(False)
                OR.setSelected(True)
                print("OR")

    print("Not a press")

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            findSelected().setPosition(x, y)



    def findSelected():
        if OR.getSelected():
            return OR
        elif AND.getSelected():
            return AND

    # Set up a label
    #label = pyglet.text.Label('Hello World!')

    # Set up an image
    #image = pyglet.image.load(path)

    # idk
    @window.event
    def on_draw():
        window.clear()
        label.draw()
        AND.draw()
        OR.draw()    
    run()

# start the application
def run():
    pyglet.app.run()
   
# idk
if __name__ == '__main__':
    main()
    
