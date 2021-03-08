import numpy as np


def X(teta, a, b):
    '''
        Множество координат х для улитки Паскаля.
    '''
    x = []
    for alpha in teta:
        x.append(a * np.cos(alpha) * np.cos(alpha) + b * np.cos(alpha))
    return x


def Y(teta, a, b):
    '''
        Множество координат у для улитки Паскаля.
    '''
    y = []
    for alpha in teta:
        y.append(a * np.cos(alpha) * np.sin(alpha) + b * np.sin(alpha))
    return y


def snail(teta, a, b):
    '''
        Функция для создания массива для улитки Паскаля.
    '''
    res = []
    x = X(teta, a, b)
    y = Y(teta, a, b)
    for i in range(len(teta)):
        res.append([x[i] - b, y[i]])
    res.append([x[0] - b, y[0]])

    return res


def hatching(snail, sh):
    '''
        Функция для создания массива для штрихов.
    '''
    x_up = [-sh * 4, -sh * 2, 0, sh, -1, sh * 2, sh * 3, sh * 4]
    y_up = [0, sh, sh * 2, sh * 3 // 2, -1, sh, sh // 2, 0]

    x_back = [-sh * 4, -sh * 3, -sh * 2, -1, -sh,  0, sh * 2, sh * 4]
    y_back = [0, -(sh // 2), -sh, -1, -(sh * 3 // 2), -sh * 2, -sh, 0]

    for i in range(len(snail)):
        if abs(1.5 * snail[i][0] - snail[i][1]) <= 0.2:
            x_back[3] = snail[i][0]
            y_back[3] = snail[i][1]
            x_up[4] = -snail[i][0]
            y_up[4] = -snail[i][1]

    res = []
    for i in range(len(x_up)):
        res.append([x_up[i], y_up[i]])
        res.append([x_back[i], y_back[i]])
    return res
