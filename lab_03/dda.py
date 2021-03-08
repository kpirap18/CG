def cda_test(p_start, p_end):
    dx = abs(p_end[0] - p_start[0])
    dy = abs(p_end[1] - p_start[1])

    if dx > dy:
        L = dx
    else:
        L = dy

    sx = (p_end[0] - p_start[0]) / L
    sy = (p_end[1] - p_start[1]) / L

    x = p_start[0]
    y = p_start[1]
    
    while abs(x - p_end[0]) > 1 or abs(y - p_end[1]) > 1:
        x += sx
        y += sy