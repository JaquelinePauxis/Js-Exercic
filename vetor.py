def multiplicacao_vetor(vetor):
    # Caso base: Se o vetor estiver vazio, retorne 1 (elemento neutro da multiplicação).
    if not vetor:
        return 1
    # Caso recursivo: Multiplique o primeiro elemento pelo resultado da recursão com um vetor menor.
    else:
        return vetor[0] * multiplicacao_vetor(vetor[1:])

# Exemplo de uso:
vetor = [2, 3, 4, 5]
resultado = multiplicacao_vetor(vetor)
print("Resultado da multiplicação:", resultado)
