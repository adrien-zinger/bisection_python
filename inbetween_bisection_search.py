from math import floor

#
# Find in an ordoned data structure the exact target's
# or the nearest's (left/right) index.
#
# target: the target
# func: the getter with an index as argument
# left: default true (useless if the exact target found)
# limits: left and right values
def btwn_bisection_search(target, func, limits, left = True):
    l, r = limits
    if l >= r or func(l) > target or func(r) < target or func(l) >= func(r):
        raise Exception("Cannot find index")
    if func(l) == target: return l
    if func(r) == target: return r
    while r - l > 1:
        m = floor((l+r) / 2)
        val = func(m)
        if val == target: return m
        if target < val: r = m
        else: l = m
    return (r, l)[left]
