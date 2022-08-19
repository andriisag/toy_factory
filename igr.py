class Factory():
       def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

       def materials(self):
           print("Купуємо сировину")
       def sew(self):
          print("Шиємо")    
       def paint(self):
           print("Фарбуємо")         

class Toy(Factory):
       def show(self):
           return f"{self.name}, {self.color}, {self.type}"


    

toy1 = Toy("Ведмідь", "Коричневий", "Тварина")

toy1.materials()
toy1.sew()
toy1.paint()
print(toy1.show())