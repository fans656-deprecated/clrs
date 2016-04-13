from clrs import *

def std(a, b):
    def to_n(a):
        return ''.join(str(t) for t in a)
    c = int(to_n(a), 2) + int(to_n(b), 2)
    c = map(int, bin(c)[2:])
    n = max(len(a), len(b)) + 1
    return ([] if len(c) == n else [0]) + c

@test
def _(f):
    def gen():
        return [1] + [random.randint(0,1)
                      for _ in xrange(random.randint(50,55))]
    for _ in xrange(100):
        a = gen()
        b = gen()
        c = f(a, b)
        if not (c == std(a, b)):
            print a, b, std(a, b), c
            raise Exception

@answer
def _(a, b):
    longer = len(a) > len(b)
    c = [0] + (a if longer else b)
    carry = 0
    for i, t in enumerate(reversed(b if longer else a)):
        c[-i-1] += carry + t
        carry = c[-i-1] // 2
        c[-i-1] = c[-i-1] % 2
    while carry:
        i += 1
        c[-i-1] += carry
        carry = c[-i-1] // 2
        c[-i-1] = c[-i-1] % 2
    return c
