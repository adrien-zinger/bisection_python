from math import floor
def binary_search(l, r):
    while l <= r:
        m = floor((l + r) / 2)
        y = yield m
        if y > 0: l = m + 1
        elif y < 0: r = m - 1
        else: return m
    return None
