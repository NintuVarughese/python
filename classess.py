class Flower:
  def __init__(self, color, name):
    self.color = color
    self.name = name

  def myfunc(self):
    print("the flower is  " + self.name)
    print("the colour of the flower is "+ self.color)

p1 = Flower("Red","Rose")
p1.myfunc()


 