candidatos = {
  'Maria' : 0,
  'João' : 0,
  'Joaquim' : 0,
  'Josefa' : 0,
  'Voto Nulo' : 0,
  'Voto em Branco' : 0
}

while True:
  print(f'{'-' * 10} CANDIDATOS E OPÇÕES {'-' * 10}')
  print('''1 - Maria
2 - João
3 - Joaquim
4 - Josefa
5 - Voto Nulo
6 - Voto em Branco
0 - Sair''')
  opcao = int(input('Digite em quem você deseja votar: '))

  if opcao == 1:
    candidatos['Maria'] += 1
  elif opcao == 2:
    candidatos['João'] += 1
  elif opcao == 3:
    candidatos['Joaquim'] += 1
  elif opcao == 4:
    candidatos['Josefa'] += 1
  elif opcao == 5:
    candidatos['Voto Nulo'] += 1
  elif opcao == 6:
    candidatos['Voto em Branco'] += 1
  elif opcao == 0:
    break
  else:
    print('Opção inválida. Digite um número das opções dadas!')

print(candidatos)

total = candidatos['Joaquim'] + candidatos['Josefa'] + candidatos['João'] + candidatos['Maria'] + candidatos['Voto em Branco'] + candidatos['Voto Nulo']

print(f'A porcetagem de votos nulos sobre o total de votos é de {(candidatos["Voto Nulo"] / total) * 100 :.2f}% e a de votos brancos sobre o total é de {(candidatos["Voto em Branco"] / total) * 100 :.2f}%')












'''numero = int(input('Montar a tabuada de: '))
comeco = int(input('Começar por: '))
termino = int(input('Terminar em: '))

while comeco <= termino:
  print(f'{numero} X {comeco} = {numero * comeco}')
  comeco += 1


chico = 1.5
ze = 1.1
tempo = 0

while ze < chico:
  chico += 0.02
  ze += 0.03
  tempo += 1

print(f'Foram necessários {tempo} anos para Zé alcança Chico em altura')
'''

