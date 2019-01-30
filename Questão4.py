import time
import random

class Fila_Banco:
  def __init__(self):
    self.fila = []
  
  def entrar(self,senha):
    self.fila.append(senha)
  
  def isEmpty(self):
    return len(self.fila) == 0

  def atendimento(self,numero):
    while not(self.isEmpty()):
      time.sleep(numero)
      print("Senha:%d"%(self.fila[0]))
      print('-=-=-=-=-=-=-')
      print("Atendido")
      print('-=-=-=-=-=-=-')
      self.fila.pop(0)
      if not(self.isEmpty()):
        print("Proximo: %d"%(self.fila[0]))
        print('-=-=-=-=-=-=-')
    print('Sessao Encerrada')
    print('-=-=-=-=-=-=-')
    print('Esperando novos clientes...')
def main():
  Banco = Fila_Banco()
  Banco.entrar(1)
  Banco.entrar(2)
  Banco.entrar(3)
  numero = random.randint(1,10)
  Banco.atendimento(numero)

if(__name__=="__main__"):
  main()
