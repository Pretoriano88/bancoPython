saldo = 0
SAQUE = 3 
num_saque = 0

def sacar(valor):
    global saldo, num_saque
    if valor > saldo:
        print("Saldo insuficiente!")

    else: 
        if num_saque <= SAQUE:
            if valor <= 500:
                
                saldo -= valor
                print(f"Saque de {valor} Realizado com sucesso !")
                num_saque +=1
            else:
                print("Valor maior excedeu o limite de 500 reais !")

        else:
            print(f"Número máximo de saques atingido ! {num_saque}")


def depositar(valor):
    global saldo 
    if valor <=0 :
        print("Digite um valor válido !")
    else:
        saldo += valor
        print(f"Deposito no valor: {valor} realizado com sucesso ! ")


def extrato():
    global saldo
    print(f"Seu saldo atual é: R${saldo:,.2f}")

while True:
    print("""Bem-vindo ao Banco Python!
          Escolha uma opção:
          1- Sacar
          2- Depositar
          3- Extrato
          4- Sair """)
    op = input("")

    if op == "1":
        value = float(input("Digite o valor do saque: "))
        sacar(value)
    elif op == "2":
        value = float(input("Digite o valor do depósito: "))
        depositar(value)
    elif op == "3":
        extrato()
    elif op == "4":
        print ("Até mais !")
        break
    else:
        print("Opção inválidda, tente novamente !")