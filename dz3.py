import math
import matplotlib.pyplot as py
# X = [x*math.sin(math.radians(x)) for x in range(10000)]
# py.plot(X)
# py.show()


# def foo():
#     for x in range(10000):
#         yield x*math.sin(math.radians(x))
#
#
# X = [x for x in foo()]

def foo():
    for x in range(10000):
        if 0 < math.radians(x) % (2*math.pi) < math.pi/2 % (2*math.pi) \
         or math.pi % (2*math.pi) < math.radians(x) % (2*math.pi) < 3*math.pi/2 % (2*math.pi):
            yield math.sin(math.radians(x))
        if math.pi/2 % (2*math.pi) < math.radians(x) % (2*math.pi) < math.pi % (2*math.pi) \
         or 3*math.pi/2 % (2*math.pi) < math.radians(x) % (2*math.pi) < 2*math.pi % (2*math.pi):
            yield math.cos(math.radians(x))


X = [x for x in foo()]
py.plot(X)
py.show()
