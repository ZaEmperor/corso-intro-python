from datetime import datetime

class Marca:


   def __init__(self, nome):
    
   def __repr__(self):

       return "<Marca %s>" % self.nome


class Automobile:

    def __init__(self, nome, anno, Marca, consumo):
       anno = int(anno)
       self.nome = nome
       self.anno = anno
       self.carburante = 0
       self.eta = datetime.now().year - anno
       self.marca = Marca(marca)
       self.consumo = int(consumo)


    def __repr__(self):
       return "<Automobile %s>" % self.nome

if __name__ == '__main__':
   import time 
   nome = raw_input("nome della macchina: ")
   anno = raw_input("anno di fabbricazione (aaaa): ")
   while len(anno) !=4:
       print "Errore nel formato dell'anno!"
       anno = raw_input("anno di fabbricazione (aaaa): ")

   def rifornisci(self, litri):
       self.carburante += litri

   def consuma(self):
       self.carburante -= self.consumo

   mia_auto = Automobile(nome, anno, marca, consumo)
   print "Quindi possiedi una %s %s" % (mia_auto.marca.nome, mia_auto.nome)


   """

   print mia_auto
   print "Costruita nel &s" % mia_auto.anno
   print "Quindi ha &s anni" % mia_auto.eta
   print "Carburante: %s litri" % mia_auto.carburante
   
   mia_auto.rifornisci(30)
   print "Carburante: %s litri" % mia_auto.carburante
  

   mia_auto.consuma(10)

   secondi = 20
   while secondi > 0:
      mia_auto.consuma(1)
      secondi -= 1
      time.sleep(1)
      print "Carburante: %s litri" % mia_auto.carburante

   
