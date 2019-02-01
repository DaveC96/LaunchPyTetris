import Launchpad
import Shapes
import yaml
import time

cfg = yaml.load(open("Config.yaml"))
lp = Launchpad.Launchpad()

def __main__():

    shapetemplates = [
        Shapes.Shape(cfg["colours"]["cyan"], [111, 121, 131, 141]),     # I
        Shapes.Shape(cfg["colours"]["blue"], [111, 112, 122, 132]),     # J
        Shapes.Shape(cfg["colours"]["orange"], [111, 112, 121, 131]),   # L
        Shapes.Shape(cfg["colours"]["yellow"], [111, 112, 121, 122]),   # O
        Shapes.Shape(cfg["colours"]["green"], [112, 121, 122, 131]),    # S
        Shapes.Shape(cfg["colours"]["purple"], [111, 121, 122, 131]),   # T
        Shapes.Shape(cfg["colours"]["red"], [111, 121, 122, 132])       # Z
    ]

    for a in shapetemplates:
        for i in range(15):
            a.move_right()
            update_board(a)
            a.move_down()
            update_board(a)
            time.sleep(.15)

def update_board(a):
    print("-BOARD UPDATE-\t\tclearing: "+str(a.last)+"\t\tdrawing: "+str(a.location))
    for i in a.last:
        lp.draw_px(i, 0)
        # l.draw_board(0)

    for i in a.location:
        lp.draw_px(i, a.colour)


__main__()