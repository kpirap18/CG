from math import sin, cos, pi, sqrt
funcs = list()

funcs.append(lambda x, z: sin(x) * sin(z))
funcs.append(lambda x, z: sin(cos(x)) * sin(z))
funcs.append(lambda x, z: cos(sqrt(x**2 + z**2)))
funcs.append(lambda x, z: sqrt(x**2 + z**2))
funcs.append(lambda x, z: cos(x) * cos(z))
funcs.append(lambda x, z: sin(z) * cos(x))

