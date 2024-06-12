class Flower:
    def __init__(self,color,name):
        self.color = color
        self.name = name
    def describe(self):
        print("rose is a flower")
class Leaf:
    def __init__(self,color,name):
        self.color = color
        self.name = name
    def describe(self):
        print("green leafs are good for vitamins")
class Tree:
    def __init__(self,color,name):
        self.color = color
        self.name = name
    def describe(self):
        print("human need tree to survive")
f1 = Flower("red","rose")
l1 = Leaf("green","neem")
t1 = Tree("yellow","yard")
for x in(f1,l1,t1):
    x.describe() 

