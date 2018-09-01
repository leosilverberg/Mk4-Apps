"""This is a simple hello world app"""

___name___         = "Hello World"
___license___      = "MIT"
___dependencies___ = ["sleep", "app", "shared/nokia.png",]
___categories___   = ["EMF"]

import ugfx, os, time, sleep, app


# initialize screen
ugfx.init()
ugfx.clear()

ugfx.text(5, 5, "Hello World!!!", ugfx.BLACK)
ugfx.display_image(0, 0, "shared/nokia.png")
