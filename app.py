import os 
from datetime import datetime

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
LIMITE_QUANTIDADE_TRANSACAO = 3
saldo = 1000    
historico = [{
  "valor": 200,
  "tipo": "Saque",
  "data": datetime(2024, 9, 27, 12, 5)
},{
  "valor": 200,
  "tipo": "Saque",
  "data": datetime(2024, 9, 27, 11, 10)
},{
  "valor": 200,
  "tipo": "Saque",
  "data": datetime(2024, 9, 28, 2, 25)
},{
  "valor": 200,
  "tipo": "Saque",
  "data": datetime(2024, 9, 28, 11, 10)
}]


def formata_data(data):
  data_formatada = data.strftime("%d/%m/%Y %H:%M")
  return data_formatada

def formatar_moeda(valor):
  return f"R$ {valor:,.2f}"

def quantidades_transacoes_diaria():
  global historico

  hoje = datetime.now().date()
  contador = sum(1 for item in historico if item.get("data").date() == hoje)
  return contador

def realizar_saque():
  global saldo
  quantidade_de_transacao = quantidades_transacoes_diaria()

  print("\nVocê escolheu sacar.")
  valor_digitado = int(input("Digite o valor: "))
  if valor_digitado > saldo:
    print("Você não possui saldo suficiente.")
  elif valor_digitado > LIMITE_DE_SAQUE:
    print(f"Seu limite por saque é de {formatar_moeda(LIMITE_DE_SAQUE)}.")
  elif quantidade_de_transacao >= LIMITE_QUANTIDADE_TRANSACAO:
    print(f"Seu limite de transações é de {LIMITE_QUANTIDADE_TRANSACAO}.") 
  else:
    saldo = saldo - valor_digitado
    print(f"Saque realizado com sucesso.\nSeu saldo atual é: {formatar_moeda(saldo)}")
    hoje = datetime.now()
    historico.append({
      "valor": valor_digitado,
      "tipo": "Saque",
      "data": hoje
    })
    

def realizar_deposito():
  global saldo
  quantidade_de_transacao = quantidades_transacoes_diaria()

  print("\nVocê escolheu depositar.")
  valor_digitado = int(input("Digite o valor que deseja depositar: "))
  if valor_digitado <= 0:
    print("Digite um valor positivo.")
  elif quantidade_de_transacao >= LIMITE_QUANTIDADE_TRANSACAO:
    print(f"Seu limite de transações é de {LIMITE_QUANTIDADE_TRANSACAO}.")
  else:
    saldo = saldo + valor_digitado
    print(f"Depósito realizado com sucesso.\nSeu saldo atual é: {formatar_moeda(saldo)}")
    hoje = datetime.now()
    historico.append({
      "valor": valor_digitado,
      "tipo": "Depósito",
      "data": hoje
    })

def apresentar_extrato():
  print("""    Extrato da conta:\n""")
  if not historico:
    print("""    Não foram realizadas movimentações.\n""")  
  else: 
    for item in historico:
      print(f"""   {item['tipo']}: {formatar_moeda(item['valor'])} .......... {formata_data(item['data'])}""")
  print(f"""   Saldo atual: {formatar_moeda(saldo)}""")
 
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