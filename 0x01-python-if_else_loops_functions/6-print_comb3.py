#!/usr/bin/python3
for y in range(0, 10):
    for x in range(y + 1, 10):
        if y == 8 and x == 9:
            print('89')
        else:
            print('{}{}, '.format(y, x), end='')
