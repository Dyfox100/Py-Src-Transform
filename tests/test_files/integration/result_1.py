test = None
i = None
loop_index0 = None
key = None


def add(a, b):
    return a + b


def function(param):
    xs = None
    ys = None
    results = None
    loop_index1 = None
    x = None
    loop_index0 = None
    y = None
    app1 = None
    z = None
    xs = [1, 2, 3, 4, 5]
    ys = [3, 5, 6, 7, 8]
    results = []
    loop_index1 = 0
    while loop_index1 < len(xs):
        x = xs[loop_index1]
        loop_index0 = 0
        while loop_index0 < len(ys):
            y = ys[loop_index0]
            app1 = add(y, 1)
            results = add(x, app1)
            loop_index0 += 1
        loop_index1 += 1
    z = 0


test = 1
i = {'key': 'val'}
loop_index0 = 0
while loop_index0 < len(i.keys()):
    key = i.keys()[loop_index0]
    pass
    loop_index0 += 1
