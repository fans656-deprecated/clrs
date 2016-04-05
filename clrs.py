import random

tester = None

def test(f):
    global tester
    tester = f

def answer(f):
    r = tester(f) or 'Accept!'
    print r
