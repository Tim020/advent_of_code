#!/usr/bin/python3

count = 0
found = False
while not found:
    index = 0
    base = None
    curr = 0
    f = open('input.txt', 'r')
    for line in f:
        curr  = int(line)
        if index == count:
	        base = int(line)
        if index != count and base is not None:
            if curr + base == 2020:
                print(curr * base)
                found = True
                break
        index += 1
    f.close()
    count += 1
