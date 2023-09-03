def teste_disponibilidade(n):
  resultado = n**3 - n
  if resultado % 3 == 0:
    return True
  else:
    return False


n = float(input("Digite um valor para n (n ≥ 1): "))

if n < 1:
  print("Por favor, insira um valor maior ou igual a 1 para n.")
else:
  divisivel_por_3 = teste_disponibilidade(n)
  if divisivel_por_3:
    print(f"{n} não é divisível por 3.")
  else:
    print(f"{n} é divisível por 3.")
