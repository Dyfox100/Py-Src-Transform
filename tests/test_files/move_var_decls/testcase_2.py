# Tests that variables are initilized at the top of scope when multiple scopes
# are available.
test = 1
def func(parameter):
    x = [1, 2, 3, 4]
    for y in x:
        z = y + 1
        while z != 0:
            z -= 1
            a = 1
        if z != 0:
            b = 1
test2 = 10
