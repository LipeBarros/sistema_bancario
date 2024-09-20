import os 

os.system("cls")

menu = """
  Bem-vindo ao Sistema Bancário Py 
      
    Opções de serviços:
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair 
       
"""

LIMITE_DE_SAQUE = 500
LIMITE_QUANTIDADE_SAQUE = 3
saldo = 100
quantidade_de_saques = 0
historico = []

def formatar_moeda(valor):
  return f"R$ {valor:,.2f}"

def realizar_saque():
  global saldo
  global quantidade_de_saques

  print("\nVocê escolheu sacar.")
  valor_digitado = int(input("Digite o valor: "))
  if valor_digitado > saldo:
    print("Você não possui saldo suficiente.")
  elif valor_digitado > LIMITE_DE_SAQUE:
    print(f"Seu limite por saque é de {formatar_moeda(LIMITE_DE_SAQUE)}.")
  elif quantidade_de_saques >= LIMITE_QUANTIDADE_SAQUE:
    print(f"Seu limite de saque diário é de {LIMITE_QUANTIDADE_SAQUE} saques.") 
  else:
    saldo = saldo - valor_digitado
    quantidade_de_saques = quantidade_de_saques + 1
    print(f"Saque realizado com sucesso.\nSeu saldo atual é: {formatar_moeda(saldo)}")
    historico.append(f"Saque: {formatar_moeda(valor_digitado)}")

def realizar_deposito():
  global saldo

  print("\nVocê escolheu depositar.")
  valor_digitado = int(input("Digite o valor que deseja depositar: "))
  if valor_digitado <= 0:
    print("Digite um valor positivo.")
  else:
    saldo = saldo + valor_digitado
    print(f"Depósito realizado com sucesso.\nSeu saldo atual é: {formatar_moeda(saldo)}")
    historico.append(f"Depósito: {formatar_moeda(valor_digitado)}")

def apresentar_extrato():
  print("""    Extrato da conta:\n""")
  if not historico:
    print("""    Não foram realizadas movimentações.\n""")
  else: 
    for item in historico:
      print(f"""    {item}""")
  print(f"""    Saldo atual: {formatar_moeda(saldo)}""")

while True:
  print(menu)
  opcao = input("Digite uma opção: ")

  if opcao == "1":
    realizar_saque()

  elif opcao == "2":
    realizar_deposito()

  elif opcao == "3":
    apresentar_extrato()

  elif opcao == "4":
    print("\nVocê escolheu sair.")

  else:
    print("\nDigite uma opção válida: ")
    
  deseja_sair = input("\nDeseja realizar outra operação? (s/n): ")  

  if deseja_sair == "n":
    break
    
  else:
    os.system("cls")

print("\nObrigado por utilizar nossos serviços.")    