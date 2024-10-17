def verifica_fibonacci(numero):
    # Inicializamos os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Enquanto 'b' for menor que o número fornecido, continuamos avançando na sequência
    while b < numero:
        # Atualizamos 'a' e 'b', onde 'a' passa a ser o valor de 'b' e 'b' passa a ser a soma de 'a' e 'b'
        a, b = b, a + b
    
    # Verificamos se 'b' é igual ao número fornecido
    if b == numero:
        return True  # Se sim, retornamos True, indicando que o número faz parte da sequência
    else:
        return False  # Caso contrário, retornamos False, indicando que o número não faz parte da sequência

# Solicitamos que o usuário insira o número que deseja verificar
numero_procurado = int(input("Digite o número que deseja verificar na sequência de Fibonacci: "))

# Verificamos se o número inserido pertence à sequência de Fibonacci
if verifica_fibonacci(numero_procurado):
    print("O número ", numero_procurado, " pertence à sequência de Fibonacci.")
else:
    print("O número ", numero_procurado, " não pertence à sequência de Fibonacci.")