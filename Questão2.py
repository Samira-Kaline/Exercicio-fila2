import time
import random 

class Fila_impressao:
  def __init__(self):
    self.fila = []
  
  def requisicao(self,documento):
    self.fila.append(documento)
  
  def isEmpty(self):
    return len(self.fila) == 0

  def impressao(self,numero):
    while not(self.isEmpty()):
      time.sleep(numero)
      print(self.fila[0])
      print('Impresso')
      self.fila.pop(0)
def main():
  Impressora = Fila_impressao()
  Impressora.requisicao('Carlos')
  Impressora.requisicao('Isaque')
  Impressora.requisicao('Kelly Ki')
  numero = random.randint(1,10)
  Impressora.impressao(numero)
 
if(__name__=="__main__"):
  main()
