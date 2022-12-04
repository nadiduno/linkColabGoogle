#Classe pai - Super classe 
class Trasnport:
  def rum(self):
    print('rum rum')
  def frar(self):
    print('freeeee')

# Clase filha, hereda os atributos do pai (transporte) pode correr e frenar como os outros transportes
#E particularmente ele pode buzinar a diferença de outros transportes
class Car(Trasnport):
  def honk(self):
    print('bibi')

c = Car()
#Posso usar os métodos do pai
print('Todos os transportes correm e freiam')
c.rum()
c.frar()
#Método propio do carro
print('\nMas não todos Buzinam')
c.honk()
