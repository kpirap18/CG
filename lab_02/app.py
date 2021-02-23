from tkinter import *
from tkinter import messagebox
import copy
from math import cos, sin, pi, sqrt


# Hides/shows axes
def hide_func(hide):
    if hide.get() == 1:
        Can.delete("all")
        draw_points(stack[-1])
    if hide.get() == 0:
        over_func(OverVar)


# Makes axes over/under picture
def over_func(over):
    if HideVar.get() == 0:
        if over.get() == 1:
            Can.delete("all")
            draw_points(stack[-1])
            draw_axes()
        if over.get() == 0:
            Can.delete("all")
            draw_axes()
            draw_points(stack[-1])


# Draws points
def draw_points(points):
    for pol in points[0]:
        Can.create_polygon(pol, fill="white", outline="black")

    for line in points[1]:
        Can.create_line(line)

    for oval in points[2]:
        Can.create_line(oval)

    for arc in points[3]:
        Can.create_line(arc)


# Creates points on default position
def get_default_points(ox, oy):
    points = [[], [], [], []]

    # Rectangles
    points[0].append([[ox - 100, oy - 50], [ox + 100, oy - 50], [ox + 100, oy], [ox - 100, oy]])

    # Lines
    points[1].append([[ox - 150, oy], [ox - 150, oy]])
    points[1].append([[ox - 150, oy + 50], [ox + 150, oy + 50]])
    points[1].append([[ox - 150, oy], [ox + 150, oy]])
    points[1].append([[ox - 40, oy - 78], [ox - 40, oy - 110]])
    points[1].append([[ox - 40, oy - 110], [ox - 10, oy - 110]])
    points[1].append([[ox - 10, oy - 110], [ox - 10, oy - 100]])
    points[1].append([[ox - 10, oy - 100], [ox - 30, oy - 100]])
    points[1].append([[ox - 30, oy - 79], [ox - 30, oy - 100]])

    # Oval:
    win1 = get_ellipse([ox - 60, oy + 25], 10, 10)
    for i in range(len(win1)):
        points[2].append(win1[i])

    win1 = get_ellipse([ox - 120, oy + 25], 10, 10)
    for i in range(len(win1)):
        points[2].append(win1[i])

    win1 = get_ellipse([ox + 120, oy + 25], 10, 10)
    for i in range(len(win1)):
        points[2].append(win1[i])

    win1 = get_ellipse([ox + 60, oy + 25], 10, 10)
    for i in range(len(win1)):
        points[2].append(win1[i])

    win1 = get_ellipse([ox, oy + 25], 10, 10)
    for i in range(len(win1)):
        points[2].append(win1[i])

    # Arc:
    arc = get_arc([ox, oy - 50], 100, 30)
    for i in range(len(arc)):
       points[3].append(arc[i])

    arc2 = get_left_arc([ox - 150, oy + 25], 30, 25)
    for i in range(len(arc2)):
        points[3].append(arc2[i])

    arc2 = get_right_arc([ox + 150, oy + 25], 30, 25)
    for i in range(len(arc2)):
        points[3].append(arc2[i])
    return points


# Creates ellipse as many lines
def get_ellipse(centre, a, b):
    circle = []
    num = 60
    step = abs(a) * 2 / num

    for i in range(num):
        x = -a + step * i
        y = sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = sqrt((1 - (x1**2)/(a**2)) * b**2)
        circle.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])
    for i in range(num):
        x = -a + step * i
        y = -sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = -sqrt((1 - (x1**2)/(a**2)) * b**2)
        circle.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    return circle


# Creates arc as many lines
def get_arc(centre, a, b):
    arc = []
    num = 60
    step = abs(a) * 2 / num

    for i in range(num):
        x = -a + step * i
        y = -sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = -sqrt((1 - (x1**2)/(a**2)) * b**2)
        arc.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    return arc

def get_left_arc(centre, a, b):
    arc = []
    num = 60
    step = abs(a) * 2 / num

    for i in range(num // 2):
        x = -a + step * i
        y = sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = sqrt((1 - (x1**2)/(a**2)) * b**2)
        arc.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    for i in range(num // 2):
        x = -a + step * i
        y = -sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = -sqrt((1 - (x1**2)/(a**2)) * b**2)
        arc.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    return arc

def get_right_arc(centre, a, b):
    arc = []
    num = 60
    step = abs(a) * 2 / num

    for i in range(num // 2, num):
        x = -a + step * i
        y = sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = sqrt((1 - (x1**2)/(a**2)) * b**2)
        arc.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    for i in range(num // 2, num):
        x = -a + step * i
        y = -sqrt((1 - (x**2)/(a**2)) * b**2)
        x1 = -a + step * (i + 1)
        y1 = -sqrt((1 - (x1**2)/(a**2)) * b**2)
        arc.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])

    return arc

# Draws axes
def draw_axes():
    Can.create_line([OX, 0], [OX, can_h])
    Can.create_line([0, OY], [can_w, OY])
    Can.create_polygon([OX, can_h], [OX - 5, can_h - 10], [OX + 5, can_h - 10])
    Can.create_polygon([can_w, OY], [can_w - 10, OY - 5], [can_w - 10, OY + 5])
    Can.create_text(OX + 15, can_h - 10, text="Y", font=Font)
    Can.create_text(can_w - 10, OY - 15, text="X", font=Font)


# Moves points, adds them in stack and rebuilds picture
def move(dx, dy):
    try:
        dx = float(dx.get())
        dy = float(dy.get())
    except ValueError:
        messagebox.showinfo("Внимание", "Неверные данные!")
        return -1

    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] += dx
                coord[1] += dy

    rebuild_scene()


# Deletes and draws picture
def rebuild_scene():
    Can.delete("all")
    if HideVar.get() == 1:
        draw_points(stack[-1])
    elif OverVar.get() == 0:
        draw_axes()
        draw_points(stack[-1])
    elif OverVar.get() == 1:
        draw_points(stack[-1])
        draw_axes()


# Prints ActionStack
def print_stack():
    print("==========STACK==========")
    print("Stack length: " + str(len(stack)))
    for points in range(len(stack)):
        print("Points №" + str(points))
        print("Polygons:")
        for i in stack[points][0]:
            print(i)
        print("Lines:")
        for i in stack[points][1]:
            print(i)
        print("Ovals:")
        for i in stack[points][2]:
            print(i)
        print("Arcs:")
        for i in stack[points][3]:
            print(i)
        print()
    print()


# Adds default points into stack and rebuilds picture
def reset():
    stack.append(get_default_points(OX, OY))
    rebuild_scene()


# Cancels last action and draws previous
def cancel():
    if len(stack) > 1:
        stack.pop(-1)
        rebuild_scene()


# Scales points, adds them in stack and rebuilds picture
def scale(kx, ky, xc, yc):
    try:
        kx = float(kx.get())
        ky = float(ky.get())
        xc = float(xc.get())
        yc = float(yc.get())
    except ValueError:
        messagebox.showinfo("Внимание", "Неверные данные!")
        return -1

    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] = (coord[0] - xc - OX) * kx + xc + OX
                coord[1] = (coord[1] - yc - OY) * ky + yc + OY

    rebuild_scene()


# Turns points, adds them in stack and rebuilds picture
def turn(xc, yc, angle):
    try:
        xc = float(xc.get())
        yc = float(yc.get())
        angle = float(angle.get())
    except ValueError:
        messagebox.showinfo("Внимание", "Неверные данные!")
        return -1

    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] -= OX
                coord[1] -= OY
                new_x = xc + (coord[0] - xc) * d_cos(angle) + (coord[1] - yc) * d_sin(angle)
                new_y = yc - (coord[0] - xc) * d_sin(angle) + (coord[1] - yc ) * d_cos(angle)
                coord[0] = new_x
                coord[1] = new_y
                coord[0] += OX
                coord[1] += OY

    rebuild_scene()


# Cos of angle from rads to degrees
def d_cos(a):
    return cos(a * pi / 180)


# Sin of angle from rads to degrees
def d_sin(a):
    return sin(a * pi / 180)


# Main window
root = Tk()
#root.resizable(False, False)
can_h = 800
can_w = 800
but_w = 250  # const

print(root.winfo_screenwidth())

root.geometry(str(can_w + but_w) + "x" + str(can_h))
root.title("Субмарина")
Font = "Arial 16"
EntryW = 10
Can = Canvas(root, height=can_h, width=can_w, bg='white')

OX = can_w / 2
OY = can_h / 2
stack = []


# Frames
Buttons = Frame(root)
Move = Frame(Buttons)
Scale = Frame(Buttons)
Turn = Frame(Buttons)
Settings = Frame(Buttons)

# Move
MoveDxVar = StringVar()
MoveDyVar = StringVar()

MoveName = Label(Move, text="Перенос:", font=Font).grid(row=0, column=0, columnspan=4)
MoveDx = Label(Move, text="dx:", font=Font).grid(row=1, column=0)
MoveDy = Label(Move, text="dy:", font=Font).grid(row=1, column=2)

MoveDxEntry = Entry(Move, width=EntryW, textvariable=MoveDxVar).grid(row=1, column=1)
MoveDyEntry = Entry(Move, width=EntryW, textvariable=MoveDyVar).grid(row=1, column=3)

MoveButton = Button(Move, text="Выполнить", font=Font, command=lambda: move(MoveDxVar, MoveDyVar)).grid(row=2, column=1, columnspan=2)

Move.grid(row=0, column=0)

# Scale
ScaleKxVar = StringVar()
ScaleKyVar = StringVar()
ScaleXcVar = StringVar()
ScaleYcVar = StringVar()

ScaleName = Label(Scale, text="Масштабирование:", font=Font).grid(row=0, column=0, columnspan=4)
ScaleKx = Label(Scale, text="Kx:", font=Font).grid(row=1, column=0)
ScaleKy = Label(Scale, text="Ky:", font=Font).grid(row=1, column=2)
ScaleXc = Label(Scale, text="Xc:", font=Font).grid(row=2, column=0)
ScaleYc = Label(Scale, text="Yc:", font=Font).grid(row=2, column=2)

ScaleKxEntry = Entry(Scale, width=EntryW, textvariable=ScaleKxVar).grid(row=1, column=1)
ScaleKyEntry = Entry(Scale, width=EntryW, textvariable=ScaleKyVar).grid(row=1, column=3)
ScaleXcEntry = Entry(Scale, width=EntryW, textvariable=ScaleXcVar).grid(row=2, column=1)
ScaleYcEntry = Entry(Scale, width=EntryW, textvariable=ScaleYcVar).grid(row=2, column=3)

ScaleButton = Button(Scale, text="Выполнить", command=lambda: scale(ScaleKxVar, ScaleKyVar, ScaleXcVar, ScaleYcVar), font=Font).grid(row=3, column=1, columnspan=2)

Scale.grid(row=1, column=0)

# Turn
TurnXcVar = StringVar()
TurnYcVar = StringVar()
TurnAngleVar = StringVar()

TurnName = Label(Turn, text="Поворот:", font=Font).grid(row=0, column=0, columnspan=4)
TurnXc = Label(Turn, text="Xc:", font=Font).grid(row=1, column=0)
TurnYc = Label(Turn, text="Yc:", font=Font).grid(row=1, column=2)
TurnAngle = Label(Turn, text="Угол:", font=Font).grid(row=2, column=0)

TurnXcEntry = Entry(Turn, width=EntryW, textvariable=TurnXcVar).grid(row=1, column=1)
TurnYcEntry = Entry(Turn, width=EntryW, textvariable=TurnYcVar).grid(row=1, column=3)
TurnAngleEntry = Entry(Turn, width=EntryW, textvariable=TurnAngleVar).grid(row=2, column=1)

TurnButton = Button(Turn, text="Выполнить", command=lambda: turn(TurnXcVar, TurnYcVar, TurnAngleVar), font=Font).grid(row=3, column=1, columnspan=2)

Turn.grid(row=2, column=0)

# Settings
HideVar = IntVar()
OverVar = IntVar()

SettingsResetButton = Button(Settings, text="Восстановить", command=lambda: reset(), font=Font).grid(row=0, column=0, columnspan=2)
SettingsCancelButton = Button(Settings, text="Отменить", command=lambda: cancel(), font=Font).grid(row=1, column=0, columnspan=2)
SettingsHide = Label(Settings, text="Скрыть оси:", font=Font).grid(row=2, column=0)
SettingsOver = Label(Settings, text="Ось сверху:", font=Font).grid(row=3, column=0)
SettingsHideCheck = Checkbutton(Settings, variable=HideVar, command=lambda: hide_func(HideVar)).grid(row=2, column=1)
SettingsOverCheck = Checkbutton(Settings, variable=OverVar, command=lambda: over_func(OverVar)).grid(row=3, column=1)

Settings.grid(row=3, column=0)


Can.grid(row=0, column=0)
Buttons.grid(row=0, column=1, sticky="nsew")

Buttons.rowconfigure(0, weight=1)
Buttons.rowconfigure(1, weight=1)
Buttons.rowconfigure(2, weight=1)
Buttons.rowconfigure(3, weight=1)
root.columnconfigure(1, weight=1)


# Main program
Points = get_default_points(OX, OY)
draw_axes()
draw_points(Points)
stack.append(Points)

root.mainloop()