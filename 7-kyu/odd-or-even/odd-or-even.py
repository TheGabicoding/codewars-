def odd_or_even(arr):
    soma=sum(arr)
    if arr == "":
        return "even"
    elif soma % 2 == 0:
        return "even"
    else:
        return "odd"