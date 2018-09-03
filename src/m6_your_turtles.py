import rosegraphics as rg
"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Anesu.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
window = rg.TurtleWindow()
wes = rg.SimpleTurtle('turtle')
wes.pen = rg.Pen('blue', 70)
al = rg.SimpleTurtle('turtle')
al.pen = rg.Pen('purple', 20)
for k in range(15):
    wes.left(25)
    wes.forward(31)
    wes.right(62)
    wes.backward(16)

    al.left(43)
    al.forward(26)
    al.right(17)
    al.backward(37)
window.close_on_mouse_click()
###############################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
