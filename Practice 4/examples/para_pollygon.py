def paral(base_para, height_para):
    area_para = base_para * height_para
    return area_para

import math

def area(side, length):
    ar = (side * length ** 2) / (4 * math.tan(math.pi / side))
    return ar



def area(b1, b2, h):
    area_trap = (b1 + b2) * h / 2