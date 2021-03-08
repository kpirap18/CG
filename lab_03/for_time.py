
def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

def float_test(ps, pf):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = dy / dx
    e = m - 1 / 2
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e >= 0:
            if pr == 1:
                x += sx
            else:
                y += sy
            e -= 1
        if e <= 0:
            if pr == 0:
                x += sx
            else:
                y += sy
        e += m

def int_test(ps, pf):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = 2 * dy
    e = m - dx
    ed = 2 * dx
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e >= 0:
            if pr == 1:
                x += sx
            else:
                y += sy
            e -= ed
        if e <= 0:
            if pr == 0:
                x += sx
            else:
                y += sy
        e += m

def smoth_test(ps, pf):
    L = 100
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = dy / dx * L
    e = L / 2
    w = L - m
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e < w:
            if pr == 0:
                x += sx
            else:
                y += sy
            e += m
        elif e >= w:
            x += sx
            y += sy
            e -= w

def cda_test(ps, pf):
    dx = abs(pf[0] - ps[0])
    dy = abs(pf[1] - ps[1])
    if dx > dy:
        L = dx
    else:
        L = dy
    sx = (pf[0] - ps[0]) / L
    sy = (pf[1] - ps[1]) / L
    x = ps[0]
    y = ps[1]
    while abs(x - pf[0]) > 1 or abs(y - pf[1]) > 1:
        x += sx
        y += sy

def vu_test(ps, pf):
    x1 = ps[0]
    x2 = pf[0]
    y1 = ps[1]
    y2 = pf[1]
    I = 100
    stairs = []
    #fills = get_rgb_intensity("black", I)
    if x1 == x2 and y1 == y2:
        flag = 1

    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    # first endpoint
    xend = round(x1)
    yend = y1 + tg * (xend - x1)
    xpx1 = xend
    ypx1 = int(yend)
    y = yend + tg

    # second endpoint
    xend = int(x2 + 0.5)
    yend = y2 + tg * (xend - x2)
    xpx2 = xend

    # main loop
    if steep:
        for x in range(xpx1, xpx2):

            y += tg
    else:
        for x in range(xpx1, xpx2):
            y += tg