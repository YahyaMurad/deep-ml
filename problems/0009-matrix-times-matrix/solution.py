import numpy as np

def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    try:
        c = np.dot(np.array(a), np.array(b))
    except:
        return -1
    return c