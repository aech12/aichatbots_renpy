# The script of the game goes in this file.

define e = Character("Eileen")
# define config.log = "AI_LOG.txt"

init python:
    renpy.log("Logging")
    print("This prints to console")

label start:
    $ print("Debug message here")
    e "You've created a new Ren'Py game."
    e "after log"

    jump chat_start
    # return
