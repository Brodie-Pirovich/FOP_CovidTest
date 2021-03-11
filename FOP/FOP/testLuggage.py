import csv
from luggageClass import *

file = open("Allowed.csv", "r")
reader = csv.reader(file)

c1 = []
c2 = []
c3 = []
cl = []


def main():
    # Create a list of all the luggage
    luggageList = CreateLuggageList()

    # Check the luggage weight and dimensions
    CheckLuggage(luggageList)

    # Write the list of luggage categories to file
    fileName = "c1.csv"
    WriteToFile(fileName, c1)
    fileName = "c2.csv"
    WriteToFile(fileName, c2)
    fileName = "c3.csv"
    WriteToFile(fileName, c3)
    fileName = "cl.csv"
    WriteToFile(fileName, cl)

    # menu
    Menu()


def CreateLuggageList():
    names = []
    weight = []
    dimensions = []
    retlist = []

    for row in reader:
        names.append(row[0])
        weight.append(int(row[1]))
        dimensions.append(row[2])

    for x in range(len(names)):
        Name = names[x]
        Weight = weight[x]
        Dimensions = dimensions[x]

        retlist.append(Luggage(Name, Weight, Dimensions))

    return retlist


def CheckLuggage(luggageList):
    for i in range (len(luggageList)):
        if(luggageList[i].weight < 7):
            if(luggageList[i].dimensions == "Very Small"):

                cl.append(luggageList[i])
                print(luggageList[i].name,"'s luggage has been moved to cl\n")

        elif(luggageList[i].weight < 30):
            if(luggageList[i].dimensions == "Small" or luggageList[i].dimensions == "Normal"):

                c1.append(luggageList[i])
                print(luggageList[i].name,"'s luggage has been moved to c1\n")

        elif(luggageList[i].weight == 30):
            if(luggageList[i].dimensions == "Small" or luggageList[i].dimensions == "Normal"):

                c2.append(luggageList[i])
                print(luggageList[i].name,"'s luggage has been moved to c2\n")

        elif(luggageList[i].weight > 30):
            if(luggageList[i].dimensions == "Normal" or luggageList[i].dimensions == "Big"):

                c3.append(luggageList[i])
                print(luggageList[i].name,"'s luggage has been moved to c3\n")

        else:
            print("Error found ", luggageList[i], "\n")


def WriteToFile(fileName, fileList):
    with open(fileName, "w", newline='') as f:
        writer = csv.writer(f)

        writer.writerow(["Name", "Weight", "Dimensions"])

        for i in range(len(fileList)):
            writer.writerow([str(fileList[i].name), str(fileList[i].weight), str(fileList[i].dimensions)])

        print("File Written", "\n")


def Menu():
    print("LUGGAGE MENU!\n")
    choice = input("Which category would you like to see? 1, 2, 3, l? and x to exit: ")

    while choice[0] != 'x':
        if(choice[0] == "1"):
            OpenFile("c1.csv")
        elif(choice[0] == "2"):
            OpenFile("c2.csv")
        elif(choice[0] == "3"):
            OpenFile("c3.csv")
        elif(choice[0] == "l"):
            OpenFile("cl.csv")
        else:
            print('Invalid selection.')
            choice = input("Which category would you like to see? c1, c2, c3, cl? and e(x)it: ")

    print('\nGOODBYE!\n')


def OpenFile(fileName):
    fileToOpen = open(fileName, "r")
    fileReader = csv.reader(fileToOpen)

    for row in fileReader:
        print(row[0])
        print(row[1])
        print(row[2], "\n")

    Menu()


main()