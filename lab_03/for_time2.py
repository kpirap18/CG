from datetime import datetime
import matplotlib.pyplot as plt
from math import sin, cos, pi, radians, fabs,  floor



def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


def setItentity(color, acc = 0):
    q = 0
    for i in range(10):
        q *= q
    return "#000000"


def RGBtoHEX(rgb):
    return '#%02x%02x%02x' % rgb


def niceRound(number):
    ret = int(number)
    if number < 0:
        if fabs(number) - abs(ret) >= 0.5:
            return ret - 1
        else:
            return ret
    else:
        if number - ret >= 0.5:
            return ret + 1
        else:
            return ret


def makeReference():
    """
        Каскадное меню->"Справка"->"Справка"
    """
    referenceWindow = Tk()
    referenceWindow.title("Справка")
    referenceLabel = Label(referenceWindow, text =
    "Лабораторная работа 3, Якуба Дмитрий, ИУ7-43Б, 2020 год.", font = fontSettingLabels)
    referenceLabel.pack()
    referenceWindow.mainloop()



def makeItentity(curCol, backColor, acc):
    R = niceRound(curCol[0] + (backColor[0] - curCol[0]) * acc)
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    G = niceRound(curCol[1] + (backColor[1] - curCol[1]) * acc)
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    B = niceRound(curCol[2] + (backColor[2] - curCol[2]) * acc)
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return rgb2hex(R, G, B)


def digitBresenham(image, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        image.put(curColorLines, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        image.put(curColorLines, (curX, curY))

        if flag:
            if acc >= 0:
                curX += stepX
                acc -= (deltaX + deltaX)
            curY += stepY
            acc += deltaY + deltaY
        else:
            if acc >= 0:
                curY += stepY
                acc -= (deltaX + deltaX)
            curX += stepX
            acc += deltaY + deltaY


def digitBresenhamArray(xStart, xEnd, yStart, yEnd, color):
    pointsArray = []

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        pointsArray.append((color, (curX, curY)))

        if flag:
            if acc >= 0:
                curX += stepX
                acc -= (deltaX + deltaX)
            curY += stepY
            acc += deltaY + deltaY
        else:
            if acc >= 0:
                curY += stepY
                acc -= (deltaX + deltaX)
            curX += stepX
            acc += deltaY + deltaY


def WuAlg(image, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        image.put(curColorLines, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = -1
    curX = xStart
    curY = yStart

    curCol = list(colors.to_rgb(curColorLines))
    backColor = list(colors.to_rgb(curColorBackground))
    for k in range(3):
        curCol[k] *= 255
        backColor[k] *= 255

    for i in range(deltaX):
        color = makeItentity(curCol, backColor, 1 + acc)
        image.put(color, (curX, curY))

        color = makeItentity(curCol, backColor, - acc)
        image.put(color, (curX, curY + stepY))
        if flag:
            if acc >= 0:
                curX += stepX
                acc -= 1
            curY += stepY
            acc += tngModule
        else:
            if acc >= 0:
                curY += stepY
                acc -= 1
            curX += stepX
            acc += tngModule


def WuAlgArray(xStart, xEnd, yStart, yEnd, color):
    pointsArray = []
    if xStart == xEnd and yStart == yEnd:
        pointsArray.append((setItentity(color), (xStart, yStart)))
        return pointsArray

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = -1
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        pointsArray.append((setItentity(color, 1 + acc), (curX, curY)))

        pointsArray.append((setItentity(color, -acc), (curX, curY + stepY)))
        if flag:
            if acc >= 0:
                curX += stepX
                acc -= 1
            curY += stepY
            acc += tngModule
        else:
            if acc >= 0:
                curY += stepY
                acc -= 1
            curX += stepX
            acc += tngModule
    return pointsArray




def stepRemovalBresenham(image, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        image.put(curColorLines, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = 1 / 2
    correction = 1 - tngModule
    curX = xStart
    curY = yStart

    curCol = list(colors.to_rgb(curColorLines))
    backColor = list(colors.to_rgb(curColorBackground))
    for k in range(3):
        curCol[k] *= 255
        backColor[k] *= 255

    for i in range(deltaX):
        color = makeItentity(curCol, backColor, acc)
        image.put(color, (curX, curY))

        if flag:
            if acc >= correction:
                curX += stepX
                acc -= correction + tngModule
            curY += stepY
            acc += tngModule
        else:
            if acc >= correction:
                curY += stepY
                acc -= correction + tngModule
            curX += stepX
            acc += tngModule


def stepRemovalBresenhamArray(xStart, xEnd, yStart, yEnd, color):
    pointsArray = []
    if xStart == xEnd and yStart == yEnd:
        pointsArray.append((setItentity(color), (xStart, yStart)))
        return pointsArray

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = 1 / 2
    correction = 1 - tngModule
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        color = setItentity(color)
        pointsArray.append((color, (curX, curY)))

        if flag:
            if acc >= correction:
                curX += stepX
                acc -= correction + tngModule
            curY += stepY
            acc += tngModule
        else:
            if acc >= correction:
                curY += stepY
                acc -= correction + tngModule
            curX += stepX
            acc += tngModule
    return pointsArray


def realBresenham(image, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        image.put(curColorLines, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = tngModule - 0.5
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        image.put(curColorLines, (curX, curY))
        if flag:
            if acc >= 0:
                curX += stepX
                acc -= 1
            curY += stepY
            acc += tngModule
        else:
            if acc >= 0:
                curY += stepY
                acc -= 1
            curX += stepX
            acc += tngModule


def realBresenhamArray(xStart, xEnd, yStart, yEnd, color):
    pointsArray = []
    if xStart == xEnd and yStart == yEnd:
        pointsArray.append((color, (xStart, yStart)))
        return pointsArray

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    tngModule = deltaY / deltaX

    acc = tngModule - 0.5
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        pointsArray.append((color, (curX, curY)))
        if flag:
            if acc >= 0:
                curX += stepX
                acc -= 1
            curY += stepY
            acc += deltaY / deltaX
        else:
            if acc >= 0:
                curY += stepY
                acc -= 1
            curX += stepX
            acc += deltaY / deltaX
    return pointsArray


def DDAline(image, xStart, xEnd, yStart, yEnd):
    if xStart == xEnd and yStart == yEnd:
        image.put(curColorLines, (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    trX = abs(deltaX)
    trY = abs(deltaY)

    if trX > trY:
        length = trX
    else:
        length = trY

    deltaX /= length
    deltaY /= length

    curX = xStart
    curY = yStart

    for i in range(length):
        image.put(curColorLines, (niceRound(curX), niceRound(curY)))
        curX += deltaX
        curY += deltaY


def DDAlineArray(xStart, xEnd, yStart, yEnd, color):
    pointsArray = []
    if xStart == xEnd and yStart == yEnd:
        pointsArray.append((color, (xStart, yStart)))
        return pointsArray

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    trX = abs(deltaX)
    trY = abs(deltaY)

    length = trX if trX > trY else trY

    deltaX /= length
    deltaY /= length

    curX = xStart
    curY = yStart

    for i in range(length):
        pointsArray.append((color, (niceRound(curX), niceRound(curY))))
        curX += deltaX
        curY += deltaY
    return pointsArray

def makeErrorDegree():
    errWindow = Tk()
    errWindow.title("Ошибка!")

    Label(errWindow, font = fontSettingLower, text = "Величина угла шага\n должно являться числом \n"
                            "с плавающей точкой").grid()

    errWindow.mainloop()

def makeErrorLength():
    errWindow = Tk()
    errWindow.title("Ошибка!")

    Label(errWindow, font = fontSettingLower, text = "Длина отрезка задаётся положительным целочисленным значением").grid()

    errWindow.mainloop()

def makeErrorCenterX():
    errWindow = Tk()
    errWindow.title("Ошибка!")

    Label(errWindow, font = fontSettingLower, text = "Координата центра по оси x\n должна являться целочисленной величиной").grid()

    errWindow.mainloop()


def makeErrorCenterY():
    errWindow = Tk()
    errWindow.title("Ошибка!")

    Label(errWindow, font = fontSettingLower, text = "Координата центра по оси y\n должна являться целочисленной величиной").grid()

    errWindow.mainloop()





def timeResearch(lenn, angle, t_lib):
    masTime = []
    curTime = 0
    for i in range(100):
        degrees = 0
        curX = 500
        curY = 200
        while abs(degrees) <= 360:
            start = datetime.now()
            DDAlineArray(500, curX, 500, curY, "#000000")
            end = datetime.now()
            curTime = curTime + (end.timestamp() - start.timestamp())
            degrees += angle
            curX = niceRound(500 - lenn * sin(radians(degrees)))
            curY = niceRound(500 + lenn * cos(radians(degrees)))
    curTime /= 100
    masTime.append(curTime)
    curTime = 0

    for i in range(100):
        degrees = 0
        curX = 500
        curY = 200
        while abs(degrees) <= 360:
            start = datetime.now()
            realBresenhamArray(500, curX, 500, curY, "#000000")
            end = datetime.now()
            curTime = curTime + (end.timestamp() - start.timestamp())
            degrees += angle
            curX = niceRound(500 - lenn * sin(radians(degrees)))
            curY = niceRound(500 + lenn * cos(radians(degrees)))
    curTime /= 100
    masTime.append(curTime)
    curTime = 0

    for i in range(100):
        degrees = 0
        curX = 500
        curY = 200
        while abs(degrees) <= 360:
            start = datetime.now()
            digitBresenhamArray(500, curX, 500, curY, "#000000")
            end = datetime.now()
            curTime = curTime + (end.timestamp() - start.timestamp())
            degrees += angle
            curX = niceRound(500 - lenn * sin(radians(degrees)))
            curY = niceRound(500 + lenn * cos(radians(degrees)))
    curTime /= 100
    masTime.append(curTime)
    curTime = 0

    for i in range(100):
        degrees = 0
        curX = 500
        curY = 200
        while abs(degrees) <= 360:
            start = datetime.now()
            stepRemovalBresenhamArray(500, curX, 500, curY, "#000000")
            end = datetime.now()
            curTime = curTime + (end.timestamp() - start.timestamp())
            degrees += angle
            curX = niceRound(500 - lenn * sin(radians(degrees)))
            curY = niceRound(500 + lenn * cos(radians(degrees)))
    curTime /= 100
    masTime.append(curTime)
    curTime = 0

    for i in range(100):
        degrees = 0
        curX = 500
        curY = 200
        while abs(degrees) <= 360:
            start = datetime.now()
            WuAlgArray(500, curX, 500, curY, "#000000")
            end = datetime.now()
            curTime = curTime + (end.timestamp() - start.timestamp())
            degrees += angle
            curX = niceRound(500 - lenn * sin(radians(degrees)))
            curY = niceRound(500 + lenn * cos(radians(degrees)))
    curTime /= 100
    masTime.append(curTime)
    curTime = 0

    # for i in range(100):
    #     degrees = 0
    #     curX = 500
    #     curY = 200
    #     while abs(degrees) <= 360:
    #         start = datetime.now()
    #         # tkinterAlg(canvasWindow, curX, 500, curY, 500)
    #         curX = niceRound(500 - lenn * sin(radians(degrees)))
    #         curY = niceRound(500 + lenn * cos(radians(degrees)))
    #         degrees += angle
    #         end = datetime.now()
    #         curTime = curTime + (end.timestamp() - start.timestamp())
    # curTime /= 100
    masTime.append(t_lib)

    plt.figure(figsize = (12, 8))
    masNames = ["ЦДА", "Брезенхем \n(дейст. коэф.)",
                "Брезенхем \n(целые коэф.)", "Брезенхем \n(с уст. ступ.)",
                "Ву", "Библиотечная функция\n PyQt5"]
    plt.rcParams['font.size'] = '12'
    plt.bar(masNames, masTime, align = "center", color='green')
    plt.title("Исследование времени выполнения\n{0} - длина отрезка; {1} - угол пучка".format(lenn, angle))
    plt.ylabel("Затраченное время")
    plt.xlabel("Алгоритм")
    plt.show()
