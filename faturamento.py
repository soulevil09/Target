# Dados de faturamento fornecidos
dados = [
    {"dia": 1, "valor": 22174.17},
    {"dia": 2, "valor": 24537.67},
    {"dia": 3, "valor": 26139.61},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.66},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.23},
    {"dia": 9, "valor": 46251.17},
    {"dia": 10, "valor": 11191.47},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.48},
    {"dia": 14, "valor": 373.78},
    {"dia": 15, "valor": 2659.76},
    {"dia": 16, "valor": 48924.24},
    {"dia": 17, "valor": 18419.26},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.18},
    {"dia": 21, "valor": 43829.17},
    {"dia": 22, "valor": 18235.69},
    {"dia": 23, "valor": 4355.07},
    {"dia": 24, "valor": 13327.10},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.83},
    {"dia": 28, "valor": 1718.12},
    {"dia": 29, "valor": 13220.50},
    {"dia": 30, "valor": 8414.61}
]

# Filtrar os dias com faturamento > 0
faturamentos = []
for d in dados:
    if d['valor'] > 0:
        faturamentos.append(d['valor'])

# Menor e maior faturamento
menor = min(faturamentos)
maior = max(faturamentos)

# Média mensal
media = sum(faturamentos) / len(faturamentos)

# Contar dias acima da média
dias_acima_da_media = 0
for d in faturamentos:
    if d > media:
        dias_acima_da_media += 1

# Exibir resultados
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")