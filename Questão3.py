from datetime import datetime
now = datetime.now()
print(now)

class Cliente():
  def __init__(self, nome, entrada):
    self.nome = nome
    self.entrada = entrada

  def __repr__(self):
    return "Cliente <nome:" + self.nome + ", entrada:" + str(self.entrada) +">"

class Fila:
  def __init__(self):
    self.lista_nome = []
    self.fila_entrada = []

  def entrar(self,nome,entrada):
    self.lista_nome.append(nome)
    self.fila_entrada.append(entrada)

  def atendimento(self,numero):
    while not(self.isEmpty()):
      time.sleep(numero)
      print("Cliente:%d"%(self.fila[0]))
      print('-=-=-=-=-=-=-')
      print("Atendido")
      print('-=-=-=-=-=-=-')
      self.fila.pop(0)
      if not(self.isEmpty()):
        print("Proximo: %d"%(self.fila[0]))
        print('-=-=-=-=-=-=-')
    print('Sessao Encerrada')
    print('-=-=-=-=-=-=-')
    print('Esperando novas ligações...')
    print("tempo de atendimento %d"%(numero))

cliente1 = Cliente("Samira", datetime.now())
print(cliente1)
cliente2 = Cliente
