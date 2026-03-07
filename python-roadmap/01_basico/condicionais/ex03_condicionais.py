# 1 - 3. Crie um programa que classifique a nota:
  #  - ≥ 9 → Excelente
  # - ≥ 7 → Bom
  # - ≥ 5 → Regular
  # - < 5 → Ruim
  
nota = float(input('Digite a nota: '))
  
if nota >= 9:
    print('Excelente!')
elif nota >=7:
  print('Bom!')
elif nota >= 5:
  print('Regular.')
else:
  print('ruim.')