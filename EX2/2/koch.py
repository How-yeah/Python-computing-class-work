"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def koch(t, order, size):
    """Draws a koch curve with length n."""
    if order == 0:
        t.fd(size)
    else:
        koch(t, order - 1, size / 3)
        t.rt(85)
        koch(t, order - 1, size / 3)
        t.lt(170)
        koch(t, order - 1, size / 3)
        t.rt(85)
        koch(t, order - 1, size / 3)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -100
bob.y = 90
bob.redraw()

for i in range(5):
    koch(bob, 5, 1000)
    bob.rt(72)

world.mainloop()
