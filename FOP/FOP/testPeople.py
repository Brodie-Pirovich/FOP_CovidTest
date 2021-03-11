import csv
from personClass import *

file = open("Assignment_data_input.csv", "r")
reader = csv.reader(file)

allowedList = []


def main():
    # Create a list of all passangers
    peopleList = CreatePeopleList()

    # Check the temperature of all passangers
    temperatureList = CheckTemp(peopleList)

    # Check for corona virus symptoms
    symptomList = CheckSymptoms(temperatureList)

    # Write the list to people that need to be isolated
    RestrictedFile(symptomList)

    # Write the list of people that are safe to travel
    AllowedFile(allowedList)


def CreatePeopleList():
    Names = []
    Weight = []
    Dimensions = []
    Temperature = []
    DryCough = []
    SourThroat = []
    RespiratoryProblems = []
    retlist = []

    for row in reader:
        Names.append(row[0])
        Weight.append(int(row[1]))
        Dimensions.append(row[2])
        Temperature.append(float(row[3]))
        DryCough.append(row[4])
        SourThroat.append(row[5])
        RespiratoryProblems.append(row[6])

    for x in range(len(Names)):
        Name = Names[x]
        LWeight = Weight[x]
        LDimensions = Dimensions[x]
        Temp = Temperature[x]
        Cough = DryCough[x]
        Throat = SourThroat[x]
        Resp = RespiratoryProblems[x]

        retlist.append(person(Name, LWeight, LDimensions, Temp, Cough, Throat, Resp))

    return retlist


def CheckTemp(personList):
    retlist = []
    for i in range(len(personList)):
        if(personList[i].getTemp() > 37):
            retlist.append(personList[i])
        else:
            allowedList.append(personList[i])

    return retlist


def CheckSymptoms(temperatureList):
    retlist = []
    symptoms = 0

    for i in range(len(temperatureList)):
        if(str(temperatureList[i].getCough()) == "Y"):
            symptoms += 1

        if(str(temperatureList[i].getThroat()) == "Y"):
            symptoms += 1

        if(str(temperatureList[i].getResp()) == "Y"):
            symptoms += 1

        if(symptoms >=2):
            retlist.append(temperatureList[i])
        else:
            allowedList.append(temperatureList[i])

        symptoms = 0
        
    return retlist


def RestrictedFile(symptomList):
    with open("Restricted.csv", "w", newline='') as f:
        writer = csv.writer(f)

        for i in range(len(symptomList)):
            writer.writerow([str(symptomList[i].name), str(symptomList[i].weight), str(symptomList[i].dimensions), str(symptomList[i].temp), str(symptomList[i].cough), str(symptomList[i].throat), str(symptomList[i].resp)])

        print("\n", "Restricted File Written", "\n")


def AllowedFile(allowedList):
    with open("Allowed.csv", "w", newline='') as f:
        writer = csv.writer(f)

        for i in range(len(allowedList)):
            writer.writerow([str(allowedList[i].name), str(allowedList[i].weight), str(allowedList[i].dimensions), str(allowedList[i].temp), str(allowedList[i].cough), str(allowedList[i].throat), str(allowedList[i].resp)])

        print("\n", "Allowed File Written", "\n")

main()