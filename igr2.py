class Factory():
       def materials(self):
           print("Купуємо сировину")
       def sew(self):
          print("Шиємо")    
       def paint(self):
           print("Фарбуємо")
class Toy(Factory):
       def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type    
class Animal(Toy):
      def show(self):
           return f"Тварина  {self.name}, {self.color}, {self.type}"
class Cartoon(Toy):
      def show(self):
           return f"Пересонаж мультфільму  {self.name}, {self.color}, {self.type}"                                       


    


toy2 = Animal("Тигр", "Рудий", "Тварина")
toy3 = Cartoon("Губка боб", "Жовтий", "Персонаж мультфільму")


toy2.materials()
toy2.sew()
toy2.paint()
print(toy2.show())
toy3.materials()
toy3.sew()
toy3.paint()
print(toy3.show())
