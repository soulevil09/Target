# Dados fornecidos
dados = [
    {'SP': 67836.43},
    {'RJ': 36678.66},
    {'MG': 29229.88},
    {'ES': 27165.48},
    {'OUTROS': 19849.53}
]

# Calcula o valor total mensal
total = 0
for estado in dados:
    for valor in estado.values():
        total += valor

# Calcula e exibe o percentual de cada estado
for estado in dados:
    for nome, valor in estado.items():
        percentual = (valor / total) * 100
        print(f"{nome}: {percentual:.2f}% do total")

    
