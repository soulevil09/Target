# Entrada da string
texto = input("Digite uma string para inverter: ")

# Inicializa uma string vazia para armazenar o resultado
inverso = ""

# Percorre a string de trás para frente usando um loop
for i in range(len(texto) - 1, -1, -1):
    inverso += texto[i]

# Exibe a string invertida
print("String invertida:", inverso)