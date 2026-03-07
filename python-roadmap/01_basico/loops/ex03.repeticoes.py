# ==========================================
# EXERCÍCIO: TABUADA DE 1 A 10
# ==========================================


# -------------------------------
# Minha solução
# -------------------------------

numero = 1
while numero <= 10:
    for i in range(0, 11):
        print(f"{numero} x{i} = {numero * i}")
    print()
    numero += 1


# -------------------------------
# Forma mais comum em Python
# -------------------------------

for numero in range(1, 11):
    for i in range(0, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()