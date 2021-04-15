from swampy.TurtleWorld import *


def koch(t, size):

    if size < 4:
        fd(t, size)
        return
    koch(t, size / 3)
    t.rt(70)
    koch(t,  size / 3)
    t.lt(150)
    koch(t, size / 3)
    t.rt(70)
    koch(t,  size / 3)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = 0
bob.y = 160
bob.redraw()
bob.rt(36)
for i in range(4):
    koch(bob, 1000)
    bob.rt(100)

bob.y = -10
bob.heading = 90
bob.redraw()

world.mainloop()
