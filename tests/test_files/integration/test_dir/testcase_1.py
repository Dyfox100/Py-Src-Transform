# Integration test for the script to run transformations on files
# and all the transformations together.

def add(a, b):
    return a + b


def function(param):
    xs = [1, 2, 3, 4, 5]
    ys = [3, 5, 6, 7, 8]
    results = []
    for x in xs:
        for y in ys:
            results = add(x, add(y, 1))
    z = 0

test = 1

i = {"key": "val"}
for key in i.keys():
    pass
