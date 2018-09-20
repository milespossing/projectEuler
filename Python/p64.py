import numpy as np
import math

def periodFinder(n):
    a0 = math.floor(math.sqrt(n))
    r = []
    current = n - a0
    while True:
        