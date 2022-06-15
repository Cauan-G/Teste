# Código que verifica se veterminado termo está presente na sequencia de fibonacci



n1, n2 = 0, 1
count = 0

# recebe o valor a ser veriificado
X = int(input("Valor"))


# recebe o número de termos a qual se quer verificar
termos = int(input("Numero de termos da sequencia em que se quer verificar "))


while count < termos:
    # exibe o valor
    print(n1)

    # verifica se o valor está presente na sequencia de fibonacci
    if (X == n1):
      print('Valor esta presente')
      break

    # faz a atualização dos valores
    aux = n1 + n2
    n1 = n2
    n2 = aux
    count += 1