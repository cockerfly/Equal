#!/usr/bin/env python
import time
a = []
b =[]
start_time = time.time()
with open('control.txt', 'r') as f, open('crc32.txt', 'r') as g:
        a = f.read().split()
        b = g.read().split()
        c = set(b)
        print( [f'{word} == {b.count(word)}' for word in a if word in c])
end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")
