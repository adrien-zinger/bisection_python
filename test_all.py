import pytest
from bisection import bisection
from bisec import bisec
from binary_search import binary_search
from inbetween_bisection_search import btwn_bisection_search

def test_bisection():
    def f(x):
        if x < 2: return -1
        elif x >= 3: return 1
        else: return 0
    r=bisection(f, 0, 10, 111)
    assert r == 2.5

def test_bisection_not_found():
    def f(x):
        if x < 3.2: return -1
        elif x >= 3.5: return 1
        else: return 0
    r=bisection(f, 0, 10, 100)
    assert r == 3.4375

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

def test_btwn_bisection_search():
    li = [1, 2, 4, 5, 6, 8, 9, 10]
    def f(i): return li[i]
    assert 2 is btwn_bisection_search(4, f, [0, len(li) - 1])
    assert 1 is btwn_bisection_search(3, f, [0, len(li) - 1])
    assert 2 is btwn_bisection_search(3, f, [0, len(li) - 1], False)
    assert 7 is btwn_bisection_search(10, f, [0, len(li) - 1], False)
    assert 0 is btwn_bisection_search(1, f, [0, len(li) - 1], False)
    with pytest.raises(Exception):
        btwn_bisection_search(0, f, [0, len(li) - 1])
    with pytest.raises(Exception):
        btwn_bisection_search(1, f, [0, 10])
    with pytest.raises(Exception):
        li = [9, 2, 4, 5, 6, 8, 9, 5]
        btwn_bisection_search(1, f, [0, 7])