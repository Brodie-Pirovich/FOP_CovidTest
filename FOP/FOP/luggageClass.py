class Luggage():

    myClass = "Luggage"

    def __init__(self, name, weight, dimensions):
        self.name = name
        self.weight = weight
        self.dimensions = dimensions
    
    def printit(self):
        print("Name: ", self.name)
        print("Weight: ", self.weight)
        print("Dimensions: ", self.dimensions, "\n")

    def getWeight(self):
        return self.weight;

    def getDimensions(self):
        return self.dimensions
   

