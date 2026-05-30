def move_zeros(lst):
    for n in lst:
        if n == 0:
            lst.remove(n)
            lst.append(0)
    return lst