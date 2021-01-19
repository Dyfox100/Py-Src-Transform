# Tests that the transformations are called once for every scope in the src.
# Transformations should be called 5 times, 1 for each function and 1 for the
# top level module scope.
test = 1
def test_func():
    a = 1
    for i in range(1):
        z = 1
    while i < 1:
        i -= 1
    def test_func2(arg):
        if arg == 1:
            return arg
        else:
            def test_func3(arg2):
                return arg2 + 1
            return test_func3(arg)
def test_func4():
    pass
