e = 1
last_e = e

iter_count = 0

while 1 + e > 1:
    last_e = e
    e /= 2
    iter_count += 1
    
print(last_e)
print(iter_count)
    