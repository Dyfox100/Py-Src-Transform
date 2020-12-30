# tests that for to while conversions work with multiple loops.
y = []
x = [1, 2, 3]
for x_item in x:
    y.append(x_item)
for y_item in y:
    x.append(y_item)
