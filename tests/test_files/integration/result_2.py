i = None
loop_index1 = None
key = None
a = None
b = None
app2 = None
app1 = None
loop_index0 = None


def add(a, b):
    return a + b


i = {'key': 'val'}
loop_index1 = 0
while loop_index1 < len(i.keys()):
    key = i.keys()[loop_index1]
    pass
    loop_index1 += 1
a = 1
b = 2
if a == b:
    app2 = add(b, 1)
    app1 = add(app2, 1)
    a = add(app1, a)
    loop_index0 = 0
    while loop_index0 < len(i.keys()):
        key = i.keys()[loop_index0]
        pass
        loop_index0 += 1
