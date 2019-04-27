def lerArquivo(fileName="agendasuspeitos.txt"):
    file = open(fileName,"r")
    conteudo = file.readlines()
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].replace("\n","")
    return conteudo

while True:
  print("Menu:")
  print("1- Ver agenda de um suspeito")
  print("2- Listar agenda apenas com suspeito incluídos")
  print("3- Visualizar reciprocidades")
  print("4- Visualizar contatos com alto nível de suspeição")
  print("5- Sair")
  op=str(input("Digite a opção desejada: "))
  print()
  if op == "1":
    print("1- Ver agenda de um suspeito")
    print()
  elif op == "2":
    print("2- Listar agenda apenas com suspeito incluídos")
    print()
  elif op == "3":
    print("3- Visualizar reciprocidades")
    print()
  elif op == "4":
    print("4- Visualizar contatos com alto nível de suspeição")
    print()
  elif op == "5":
    break
    print()
  else:
    print("Opção incorreta! Tente novamente.")
    print()
