# coding: utf-8
from clrs import *
import random

u'''
找出一个数组中出现次数过半的元素

元素的取值范围未知，少数派元素也可能重复
'''

def majority(a):
    r = None
    count = 0
    for t in a:
        if count == 0:
            r = t
            count += 1
        else:
            if t == r:
                count += 1
            else:
                count -= 1
    return r

@check
def _():
    a = case.a()
    x = random.choice(a)
    a += [x] * len(a)
    random.shuffle(a)
    y = majority(a)
    yield x == y
