def lerArquivo(fileName="agendasuspeitos.txt"):
    file = open(fileName,"r")
    conteudo = file.readlines()
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].replace("\n","")
    return conteudo
    
def imprimeAgenda(nome,agenda):
    tam=len(agenda)
    for i in range(tam):
      if agenda[i].find(nome)>=0:
        ind=i
        pos=agenda[i].find(nome)
    print("Agenda do suspeito %s:" %nome)
    agendasus=agenda[ind][(len(nome)+13):]
    agendasus=agendasus.split(",")
    return agendasus

while True:
  #MENU
  print("Menu:")
  print("1- Ver agenda de um suspeito")
  print("2- Listar agenda apenas com suspeito incluídos")
  print("3- Visualizar reciprocidades")
  print("4- Visualizar contatos com alto nível de suspeição")
  print("5- Sair")
  op=str(input("Digite a opção desejada: "))
  print()
  #quebra do arquivo em duas listas agenda e chamadas
  conteudo=lerArquivo()
  pos=conteudo.index("chamadas")
  agenda=conteudo[0:pos]
  chamadas=conteudo[pos:]

  if op == "1":
    nome=str(input("Nome do suspeito: "))
    print()
    #chamando a função imprimeAgenda
    agendasus=imprimeAgenda(nome,agenda)
    for e in agendasus:
      print(e)
    print()
  elif op == "2":
    #chamar função agenda com suspeitos
    print("2- Listar agenda apenas com suspeito incluídos")
    print()
  elif op == "3":
    #chamar função reciproca
    print("3- Visualizar reciprocidades")
    print()
  elif op == "4":
    #chamar função nível de suspeição
    print("4- Visualizar contatos com alto nível de suspeição")
    print()
  elif op == "5":
    break
    print()
  else:
    print("Opção incorreta! Tente novamente.")
    print()
