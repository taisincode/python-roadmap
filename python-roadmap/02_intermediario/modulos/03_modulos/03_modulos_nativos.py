import random
from datetime import datetime

# número aleatório (1 a 100)
numero = random.randint(1, 100)
print(f"Número aleatório: {numero}")

# data atual formatada
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data atual: {data_formatada}")