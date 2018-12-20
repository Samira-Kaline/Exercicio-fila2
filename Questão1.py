class Pilha():
 def __init__(self):
   self.pilha = []

 def lenght(self):
   return len(self.pilha)

 def isEmpyt(self):
   return self.lenght()==0

 def push(self, item):
   self.pilha.append(item)

 def pop():
   self.pilha


class Fila():
 def __init__(self):
   self.fila = []
 def enqueue(self,item):
   self.fila.append(item)

 def dequeue(self):
   if not(self.isEmpty()):
     self.fila.pop(0)

 def lenght(self):
   return len(self.fila)

 def isEmpty(self):
   return self.lenght() == 0

 def peek(self):
   return self.fila[0]

 def inverter(self):
    pilha = Pilha()
    for i in range(self.lenght()-1,-1,-1):
      pilha.push(self.fila[i])
    print(pilha.pilha)
  
     


fila = Fila()
fila.enqueue("Isaque")
fila.enqueue("Fernanda")
fila.enqueue("Samira")
print(fila.fila)
fila.inverter()
