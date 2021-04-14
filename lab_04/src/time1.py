
from math import *
import matplotlib.pyplot as plt
from matplotlib import colors
from colormap import rgb2hex
from datetime import datetime
# from shittyFuncs import niceRound

curColorLines = "#000000"
curColorBackground = "#ffffff"

def reflectPointsXY1(pointsArray, xCenter, yCenter):
    prevLen = len(pointsArray)
    for i in range(prevLen):
        pointsArray.append((pointsArray[i][1] - yCenter + xCenter, pointsArray[i][0] - xCenter + yCenter,
                            pointsArray[i][2]))


def reflectPointsY1(pointsArray, xCenter):
    prevLen = len(pointsArray)
    for i in range(prevLen):
        pointsArray.append((-(pointsArray[i][0] - xCenter) + xCenter, pointsArray[i][1], pointsArray[i][2]))


def reflectPointsX1(pointsArray, yCenter):
    prevLen = len(pointsArray)
    for i in range(prevLen):
        pointsArray.append((pointsArray[i][0], -(pointsArray[i][1] - yCenter) + yCenter, pointsArray[i][2]))


def middlePointEllipseAlg(xCenter, yCenter, radiusX, radiusY, colour = "#000000"):
    pointsArray = []

    sqrRadX = radiusX * radiusX
    sqrRadY = radiusY * radiusY

    limit = round(radiusX / sqrt(1 + sqrRadY / sqrRadX))

    curX = 0
    curY = radiusY
    pointsArray.append((curX + xCenter, curY + yCenter, colour))

    func = sqrRadY - round(sqrRadX * (radiusY - 1 / 4))
    while curX < limit:
        if func > 0:
            curY -= 1
            func -= sqrRadX * curY * 2

        curX += 1
        func += sqrRadY * (curX + curX + 1)
        pointsArray.append((curX + xCenter, curY + yCenter, colour))

    limit = round(radiusY / sqrt(1 + sqrRadX / sqrRadY))

    curX = radiusX
    curY = 0
    pointsArray.append((curX + xCenter, curY + yCenter, colour))

    func = sqrRadX - round(sqrRadY * (curX - 1 / 4))
    while curY < limit:
        if func > 0:
            curX -= 1
            func -= 2 * sqrRadY * curX

        curY += 1
        func += sqrRadX * (curY + curY + 1)
        pointsArray.append((curX + xCenter, curY + yCenter, colour))

    reflectPointsX1(pointsArray, yCenter)
    reflectPointsY1(pointsArray, xCenter)

    return pointsArray


def bresenhamEllipseAlg(xCenter, yCenter, radiusX, radiusY, colour = "#000000"):
    pointsArray = []

    curX = 0
    curY = radiusY

    sqrRadX = radiusX * radiusX
    sqrRadY = radiusY * radiusY

    pointsArray.append((curX + xCenter, curY + yCenter, colour))

    delta = sqrRadY - sqrRadX * (radiusY + radiusY + 1)
    while curY > 0:
        if delta <= 0:
            negDek = delta + delta + sqrRadX * (curY + curY - 1)
            curX += 1
            delta += sqrRadY * (curX + curX + 1)
            if negDek >= 0:
                curY -= 1
                delta += sqrRadX * (-curY - curY + 1)
        else:
            posDek = delta + delta + sqrRadY * (-curX - curX - 1)
            curY -= 1
            delta += sqrRadX * (-curY - curY + 1)
            if posDek < 0:
                curX += 1
                delta += sqrRadY * (curX + curX + 1)
        pointsArray.append((curX + xCenter, curY + yCenter, colour))

    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)

    return pointsArray


def parameterEllipseAlg(xCenter, yCenter, radiusX, radiusY, colour = "#000000"):
    pointsArray = []

    if radiusX > radiusY:
        step = 1 / radiusX
    else:
        step = 1 / radiusY

    i = 0
    while i <= pi / 2 + step:
        curX = xCenter + radiusX * cos(i)
        curY = yCenter + radiusY * sin(i)
        pointsArray.append((curX, curY, colour))

        i += step

    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)
    return pointsArray


def canonicalEllipseAlg(xCenter, yCenter, radiusX, radiusY, colour = "#000000"):
    pointsArray = []

    sqrRadX = radiusX * radiusX
    sqrRadY = radiusY * radiusY
    sqrMix = sqrRadX * sqrRadY

    limitX = round(xCenter + radiusX / sqrt(1 + sqrRadY / sqrRadX))
    limitY = round(yCenter + radiusY / sqrt(1 + sqrRadX / sqrRadY))

    for curX in range(xCenter, limitX):
        curY = yCenter + sqrt(sqrMix - (curX - xCenter) * (curX - xCenter) * sqrRadY) / radiusX
        pointsArray.append((curX, curY, colour))

    for curY in range(limitY, yCenter - 1, -1):
        curX = xCenter + sqrt(sqrMix - (curY - yCenter) * (curY - yCenter) * sqrRadX) / radiusY
        pointsArray.append((curX, curY, colour))

    reflectPointsX1(pointsArray, xCenter)
    reflectPointsY1(pointsArray, yCenter)
    return pointsArray


def middlePointCircleAlg(xCenter, yCenter, radius, colour = "#000000"):
    pointsArray = []

    curX = radius
    curY = 0
    pointsArray.append((curX + xCenter, curY + yCenter, colour))

    func = 1 - radius

    while curY < curX:
        curY += 1
        if func > 0:
            curX -= 1
            func -= curX - 2 + curX

        func += curY + curY + 3
        pointsArray.append((curX + xCenter, curY + yCenter, colour))
    reflectPointsXY1(pointsArray, xCenter, yCenter)
    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)
    return pointsArray


def bresenhamCircleAlg(xCenter, yCenter, radius, colour = "#000000"):
    pointsArray = []

    curX = 0
    curY = radius
    pointsArray.append((curX + xCenter, curY + yCenter, colour))

    delta = 2 - radius - radius
    while curX < curY:
        if delta <= 0:
            d = delta + delta + curY + curY - 1
            curX += 1
            if d >= 0 :
                curY -= 1
                delta += 2 * (curX - curY + 1)
            else:
                delta += curX + curX + 1
        else:
            d = delta - curX + delta - curX - 1
            curY -= 1
            if d < 0:
                curX += 1
                delta += curX + curX - curY - curY + 2
        pointsArray.append((curX + xCenter, curY + yCenter, colour))

    reflectPointsXY1(pointsArray, xCenter, yCenter)
    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)
    return pointsArray


def parameterCircleAlg(xCenter, yCenter, radius, colour = "#000000"):
    pointsArray = []
    angleStep = 1 / radius
    i = 0
    while i <= pi / 4 + angleStep:
        curX = xCenter + radius * cos(i)
        curY = yCenter + radius * sin(i)
        pointsArray.append((curX, curY, colour))
        i += angleStep

    reflectPointsXY1(pointsArray, xCenter, yCenter)
    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)
    return pointsArray


def canonicalCircleAlg(xCenter, yCenter, radius, colour = "#000000"):
    pointsArray = []
    sqrRad = radius * radius
    for curX in range(xCenter, round(xCenter + radius / sqrt(2)) + 1):
        curY = yCenter + sqrt(radius * radius - (curX - xCenter) * (curX - xCenter))
        pointsArray.append((curX, curY, colour))
    reflectPointsXY1(pointsArray, xCenter, yCenter)
    reflectPointsY1(pointsArray, xCenter)
    reflectPointsX1(pointsArray, yCenter)
    return pointsArray





def ellipseTimeResearch(canvasWindow):
    masTime = []
    masAllTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            canonicalEllipseAlg(500, 500, i, i + 250, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.015 and not curTime < prev - 0.015:
            print(1)
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            parameterEllipseAlg(500, 500, i, i + 250, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.015 and not curTime < prev - 0.015:
            print(2)
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            bresenhamEllipseAlg(500, 500, i, i + 250, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.015 and not curTime < prev - 0.015:
            print(3)
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            middlePointEllipseAlg(500, 500, i, i + 250, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.015 and not curTime < prev - 0.015:
            print(4)
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    masAllTime.append(masTime)

    fig = plt.figure(figsize = (18, 10))
    plot = fig.add_subplot()
    ran = []
    for i in range(1, 10002, 250):
        ran.append(i)

    plot.plot(ran, masAllTime[0], label = "Алгоритм Брезенхема")
    plot.plot(ran, masAllTime[1], label = "Алгоритм на основе параметрического уравнения")
    plot.plot(ran, masAllTime[2], label = "Алгоритм на основе канонического уравнения")
    plot.plot(ran, masAllTime[3], label = "Алгоритм средней точки")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов построения эллипсов")
    plt.ylabel("Затраченное время (секунды)")
    plt.xlabel("Ширина эллипса (высота увеличивается прапорционально) (пикселы)")
    plt.show()


def circleTimeResearch(canvasWindow):
    masTime = []
    masAllTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            canonicalCircleAlg(500, 500, i, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.01 and not curTime < prev - 0.01:
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            parameterCircleAlg(500, 500, i, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.01 and not curTime < prev - 0.01:
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            bresenhamCircleAlg(500, 500, i, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.01 and not curTime < prev - 0.01:
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    curTime = 0
    masAllTime.append(masTime)
    masTime = []
    i = 1
    prev = 0

    while i <= 10001:
        curTime = 0
        for j in range(10):
            timeTempStart = datetime.now()
            middlePointCircleAlg(500, 500, i, curColorLines)
            timeTempEnd = datetime.now()
            curTime += timeTempEnd.timestamp() - timeTempStart.timestamp()
        if not curTime > prev + 0.01 and not curTime < prev - 0.01:
            prev = curTime
            curTime /= 10
            masTime.append(curTime)
            i += 250

    masAllTime.append(masTime)

    fig = plt.figure(figsize = (18, 10))
    plot = fig.add_subplot()
    ran = []
    for i in range(1, 10002, 250):
        ran.append(i)

    plot.plot(ran, masAllTime[0], label = "Алгоритм Брезенхема")
    plot.plot(ran, masAllTime[1], label = "Алгоритм на основе параметрического уравнения")
    plot.plot(ran, masAllTime[2], label = "Алгоритм на основе канонического уравнения")
    plot.plot(ran, masAllTime[3], label = "Алгоритм средней точки")
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов построения окружностей")
    plt.ylabel("Затраченное время (секунды)")
    plt.xlabel("Длина радиуса (пикселы)")
    plt.show()