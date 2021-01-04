y = []
x = [1, 2, 3]
loop_index0 = 0
while loop_index0 < len(x):
    x_item = x[loop_index0]
    y.append(x_item)
    loop_index0 += 1
loop_index1 = 0
while loop_index1 < len(y):
    y_item = y[loop_index1]
    x.append(y_item)
    loop_index1 += 1
