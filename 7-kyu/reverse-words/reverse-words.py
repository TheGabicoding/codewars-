def reverse_words(text):
    cortado = text.split(' ')
    invertido = [p[::-1] for p in cortado]
    return ' '.join(invertido)