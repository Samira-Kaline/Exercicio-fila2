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
    Impresso = False
    if not(self.isEmpty()):
      time.sleep(numero)
      print("Documento: %s "%(self.fila[0]))
      self.fila.pop(0)
      Impresso = True
    return Impresso
      
def main():
  Impressora = Fila_impressao()
  opcao = 0
  while(opcao!=3):
    print("1-Requerir uma impressao")
    print('2-Imprimir')
    print("3-Sair")
    opcao = int(input())
    if(opcao==1):
      Documento = input("Digite o nome do Documento: ")
      Impressora.requisicao(Documento)
      print("Documento adicionado")
    elif(opcao==2):
      inicio = time.time()
      print("Imprimindo...")
      numero = random.randint(1,10)
      Impresso = Impressora.impressao(numero)
      if(Impresso):
        print("Impresso!")
      else:
        print("Nao tem documento, "+
          "Por favor, Digite 1 Para Requerir uma Impressao")
      fim = time.time()
      print("Tempo de Impressao: %f"%(fim-inicio))
 
if(__name__=="__main__"):
  main()
