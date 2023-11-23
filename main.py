import random
numero_atual = random.randint (1, 100)
print(f"O número atual é {numero_atual}.")
proximo_numero = random.randint(1,100)
escolha = input("O próximo número será maior ou menor? " )
print(f"O próximo número é { proximo_numero}.")
if escolha == "maior" and proximo_numero > numero_atual:
  print('voce acertou!')
elif escolha == "menor" and proximo_numero < numero_atual:
  print('voce acertou!')
if escolha != "menor" and proximo_numero < numero_atual:
  print('voce errou!')
elif escolha != "maior" and proximo_numero > numero_atual:
  print('voce errou!')
