from datetime import datetime
import random
import time

class Cliente():
  def __init__(self, nome, entrada):
    self.nome = nome
    self.entrada = entrada


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
      print("Cliente:%s"%(self.lista_nome[0]))
      print('-=-=-=-=-=-=-')
      print("hora de entrada: %s"%(self.fila_entrada[0]))
      print("Atendido")
      print('-=-=-=-=-=-=-')
      print("tempo de atendimento: %s segundos"%(numero))
      print('-=-=-=-=-=-=-')
      print("hora de saida: %s"%(datetime.now()))
      print('-=-=-=-=-=-=-')
      self.lista_nome.pop(0)
      self.fila_entrada.pop(0)
      if not(self.isEmpty()):
        print("Proximo: %s"%(self.lista_nome[0]))
        print('-=-=-=-=-=-=-')
    print('Sessao Encerrada')
    print('-=-=-=-=-=-=-')
    print('Esperando novas ligações...')

  def isEmpty(self):
    return len(self.lista_nome) == 0
def main():
  cliente1 = Cliente("Samira", datetime.now())
  time.sleep(2)
  cliente2 = Cliente("Douglas",datetime.now())

  fila = Fila()
  fila.entrar(cliente1.nome,cliente1.entrada)
  fila.entrar(cliente2.nome,cliente2.entrada)
  numero = random.randint(1,10)
  fila.atendimento(numero)

if(__name__=="__main__"):
  main()
