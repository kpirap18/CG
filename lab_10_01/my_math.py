from math import cos, pi, sin


def sign(x):
    if not x:
        return 0
    else:
        return x / abs(x)


def turn_x(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = y
    y = cos(alpha) * y - sin(alpha) * z
    z = cos(alpha) * z + sin(alpha) * buf
    return x, y, z
        

def turn_y(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = x
    x = cos(alpha) * x - sin(alpha) * z
    z = cos(alpha) * z + sin(alpha) * buf
    return x, y, z


def turn_z(x, y, z, alpha):
    alpha = alpha * pi / 180
    buf = x
    x = cos(alpha) * x - sin(alpha) * y
    y = cos(alpha) * y + sin(alpha) * buf
    return x, y, z


def transform(x, y, z, alpha_x, alpha_y, alpha_z, scale_k, w, h):
    # print("transform", scale_k, w, h)
    x, y, z = turn_x(x, y, z, alpha_x)
    x, y, z = turn_y(x, y, z, alpha_y)
    x, y, z = turn_z(x, y, z, alpha_z)
    # print(x, y, z)
    x = x * scale_k + w / 2 
    y = y * scale_k + h / 2 
    # print("transform end", x, y, z)
    return round(x), round(y), round(z)