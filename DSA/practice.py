def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
show(5)


def show(n):
    if n == 0:
        return
    print(n-1)
    show(n-1)
show(5)



