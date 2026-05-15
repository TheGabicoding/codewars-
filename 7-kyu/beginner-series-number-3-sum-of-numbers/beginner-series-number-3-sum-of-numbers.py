def get_sum(a, b):
    menor = min(a, b)
    maior = max(a, b)
    return sum(range(menor, maior + 1))