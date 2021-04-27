import pytest
from bisection import bisection
from bisec import bisec
from binary_search import binary_search

def test_bisection():
    def f(x):
        if x < 5: return -1
        elif x >= 6: return 1
        else: return 0
    r=bisection(f, 0, 10, 1)
    print(r)
    assert r==5

def test_bisec():
    def f(x):
        if x < 5: return -1
        elif x >= 6: return 1
        else: return 0
    r=bisec(f, 0, 10, 1)
    print(r)
    assert r==5

def test_binary_search():
    def f(x):
        if x < 5: return -1
        elif x >= 6: return 1
        else: return 0
    bs = binary_search(0, 10)
    for m in bs:
        y = f(m)
        if y == 0: break
        bs.send(y)
    assert m==5
