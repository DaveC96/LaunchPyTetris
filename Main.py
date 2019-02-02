import Launchpad
import Shapes
import ButtonHandler
import yaml
import time

cfg = yaml.load(open("Config.yaml"))
lp = Launchpad.Launchpad()

shapetemplates = [
    Shapes.Shape(cfg["colours"]["cyan"], [111, 121, 131, 141]),  # I
    Shapes.Shape(cfg["colours"]["blue"], [111, 112, 122, 132]),  # J
    Shapes.Shape(cfg["colours"]["orange"], [111, 112, 121, 131]),  # L
    Shapes.Shape(cfg["colours"]["yellow"], [111, 112, 121, 122]),  # O
    Shapes.Shape(cfg["colours"]["green"], [112, 121, 122, 131]),  # S
    Shapes.Shape(cfg["colours"]["purple"], [111, 121, 122, 131]),  # T
    Shapes.Shape(cfg["colours"]["red"], [111, 121, 122, 132])  # Z
]

board_model = [[],[],[],[],[],[],[],[]]
for i in range(8):
    for j in range(8):
        board_model[i].append(00)

a = shapetemplates[5]

def __main__():
    # for a in shapetemplates:
    #     for i in range(15):
    #         a.move_right()
    #         update_board(a)
    #         a.move_down()
    #         update_board(a)
    #         time.sleep(.1)

    b = ButtonHandler.ButtonHandler(lp, uicallbacks)
    b.start()
    print(board_model)

def update_board(a):
    print("-BOARD UPDATE-\t\tclearing: "+str(a.last)+"\t\tdrawing: "+str(a.location))
    for i in a.last:
        lp.draw_px(i, 0)
        # l.draw_board(0)
        board_model[int(str(i)[0])][int(str(i)[1])] = 0

    for i in a.location:
        print("x: " + str(i)[1] + " y: " + str(i)[0])
        lp.draw_px(i, a.colour)
        board_model[int(str(i)[1])][int(str(i)[0])] = a.colour
        for i in range(len(board_model)):
            print(board_model[i])


    print(board_model)



def ui_flip():
    print("Flip")

def ui_left():
    print("Left")
    a.move_left()
    update_board(a)

def ui_down():
    print("Down")
    a.move_down()
    update_board(a)

def ui_right():
    print("Right")
    a.move_right()
    update_board(a)

uicallbacks = {
    1:ui_flip,
    6:ui_left,
    7:ui_down,
    8:ui_right
}

__main__()