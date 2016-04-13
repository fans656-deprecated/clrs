import random
import threading
from PySide.QtCore import *
from PySide.QtGui import *

def draw_array(p, rc, a, mi, ma):
    n = len(a)
    extent = float(ma - mi)
    item_width = float(rc.width() - (n - 1)) / n
    color = QColor(0,0,0)
    for i, v in enumerate(a):
        ratio = (v - mi) / extent
        x = rc.left() + i * (item_width + 1)
        height = rc.height() * ratio
        y = rc.bottom() - height
        p.fillRect(QRectF(x, y, item_width, height), color)

class Widget(QDialog):

    def __init__(self, th, a, parent=None):
        super(Widget, self).__init__(parent)
        a.callback = self.update_and_wait
        self.th = th
        self.a = a
        self.lock = threading.Semaphore(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)
        self.timer.start(30)
        self.mi, self.ma = min(a), max(a)
        th.start()

    def keyPressEvent(self, ev):
        if ev.text() == 'j':
            self.timeout()
            print '_'

    def timeout(self):
        self.lock.release()

    def paintEvent(self, e):
        p = QPainter(self)
        draw_array(p, self.rect(), self.a, self.mi, self.ma)

    def update_and_wait(self):
        self.update()
        self.lock.acquire()

class Array(object):

    def __init__(self, a):
        self.a = a

    def __getitem__(self, i):
        return self.a[i]

    def __setitem__(self, i, v):
        self.a[i] = v
        self.callback()

    def __iter__(self):
        return iter(self.a)

    def __len__(self):
        return len(self.a)

def vis(f):
    global a
    a = Array(a)
    def f_():
        f(a)
    th = threading.Thread(target=f_)
    th.daemon = True

    app = QApplication([])
    w = Widget(th, a)
    w.show()
    app.exec_()

def insertion_sort(a):
    for i, t in enumerate(a[1:]):
        while i >= 0 and a[i] > t:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = t

def selection_sort(a):
    for i in xrange(len(a) - 1):
        mi = i
        for j in xrange(i + 1, len(a)):
            if a[j] < a[mi]:
                mi = j
        if i != mi:
            t = a[mi]
            a[mi] = a[i]
            a[i] = t

def merge_sort(a):
    def sort(a, beg, end):
        if beg + 1 >= end:
            return
        mid = (end + beg) // 2
        sort(a, beg, mid)
        sort(a, mid, end)
        b = []
        i, j = beg, mid
        while i < mid and j < end:
            if a[i] < a[j]:
                b.append(a[i])
                i += 1
            else:
                b.append(a[j])
                j += 1
        while i < mid:
            b.append(a[i])
            i += 1
        while j < end:
            b.append(a[j])
            j += 1
        a[beg:end] = b
        return a
    return sort(a, 0, len(a))

def bubble_sort(a):
    for end in xrange(len(a) - 1, 0, -1):
        for i in xrange(end):
            if a[i] > a[i + 1]:
                t = a[i]
                a[i] = a[i + 1]
                a[i + 1] = t
    return a

def bubble_sort_2(a):
    n = len(a)
    for i in xrange(n - 1):
        for j in xrange(n - 1, i, -1):
            if a[j] < a[j - 1]:
                t = a[j]
                a[j] = a[j - 1]
                a[j - 1] = t
    return a

n = 100
a = [random.randint(1,n) for _ in xrange(n)]
#a = [5,4,1,3,2]
#vis(insertion_sort)
#vis(selection_sort)
#vis(merge_sort)
#vis(bubble_sort)
vis(bubble_sort_2)
