class Person:

    def init(self, x, y):
 
        self.a1 = x
        self.a2 = y
        
p1 = Person("Nia", 21)
  
print (p1.x, p1.y)

p1.__init__("12",2)
