class fruits:
    # contractor method
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

#method
    def display(self):
            print (f"I love eating {self.name}, it costs {self.price} and its  {self.color} in color")
#structure
myobj=fruits("banana", 20, "yellow")
myobj.display()
myobj2=fruits("Mangoes", 30, "orange")
myobj2.display()