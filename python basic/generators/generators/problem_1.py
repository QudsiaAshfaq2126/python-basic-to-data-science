def next_sq():
    i=1
    while True:
        yield i*i
        i=i+1
for n in next_sq():
    if n>25:
        break
    print(n)
