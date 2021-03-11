class person():

    myClass = "Person"

    def __init__(self, name, weight, dimensions, temp, cough, throat, resp):
        self.name = name
        self.weight = weight
        self.dimensions = dimensions
        self.temp = temp
        self.cough = cough
        self.throat = throat
        self.resp = resp

    def printit(self):
        print("Name: ", self.name)
        print("Temperature: ", self.temp)
        print("DryCough: ", self.cough)
        print("SourThroat: ", self.throat)
        print("RespiratoryProblems: ", self.resp, "\n")

    def getTemp(self):
        return self.temp;

    def getCough(self):
        return self.cough

    def getThroat(self):
        return self.throat

    def getResp(self):
        return self.resp