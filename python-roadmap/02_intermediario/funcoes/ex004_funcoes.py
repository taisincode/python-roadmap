#4: função que receba args e retorne média.

def media(*valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

print(media(2, 4, 6))  