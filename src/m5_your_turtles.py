"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhai Yihu.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
dave = rg.SimpleTurtle('turtle')
dave.pen = rg.Pen('red', 3)
dave.speed = 10
size1 = 200
matt = rg.SimpleTurtle('turtle')
matt.pen = rg.Pen('blue', 3)
matt.speed = 10
matt.left(45)
size2 = 282
for k in range(10):
    dave.draw_circle(size1)
    dave.pen_up()
    dave.left(90)
    dave.forward(10)
    dave.right(90)
    dave.pen_down()
    size1 = size1 - 10
    matt.draw_square(size2)
    matt.pen_up()
    matt.left(45)
    matt.forward(10)
    matt.right(45)
    matt.pen_down()
    size2 = size2 - 14

window.close_on_mouse_click()
