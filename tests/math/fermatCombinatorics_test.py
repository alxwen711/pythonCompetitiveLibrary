import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from src.math.fermatCombinatorics import *


def test_basic():
    r = 100000007
    facts,invs = fermat_array(100,100,r)
    n = 10
    k = 0
    assert fermat_comb(n,k,r,facts,invs) == 1
    assert fermat_comb(5,2,r,facts,invs) == 10


def test_speed():
    r = 1000000007
    facts,invs = fermat_array(200000,200000,r)
    assert fermat_comb(5,2,r,facts,invs) == 10


def test_basic():
    assert fermat_calc(8,6,100000007) == 28

def test_larger():
    assert fermat_calc(100,50,998244353) == 198626801

def test_negative():
    assert fermat_calc(7,27,11) == 0



