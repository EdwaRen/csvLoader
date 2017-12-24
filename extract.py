#!/bin/env python

import csv
import numpy
import glob, os

#Numpy can be installed here http://sourceforge.net/projects/numpy/files/NumPy/


names_f = []
names_l = []

Software = []
SensorFusion = []
Perception = []
Prediction = []
Local = []
Path = []
Simulation = []
User = []
Embedded = []
Signals = []
Vehicle = []
SensorMount = []
Internal = []
Marketing = []
Finance = []
Sponsorship = []
Website = []
Graphic = []

e = [[]]
x = 0

def removeDupe(s):
    a = [Software, SensorFusion, Perception, Prediction, Local, Path, Simulation, User, Embedded, Signals, Vehicle, SensorMount, Internal, Marketing, Finance, Sponsorship, Website, Graphic]
    # print(a[1][1][35])
    i = 0
    while i < len(a):
        x = 0
        while x < len(a[i]): #a[i][x] is an applicant
            j = x
            while j < len(a[i]):
                # print("\n", i, x, j)
                if i == len(a):
                    break
                elif x == len(a[i]):
                    break
                elif j == len(a[i]):
                    break

                if a[i][x][35] == a[i][j][35] and j != x:
                    # print("\n Popped: ", i, x, j)
                    a[i].pop(x)

                j = j+1
            x = x+1
        i = i+1


def writeCSV(s):
    f = ["Software Interface Management", "Sensor Fusion", "Perception", "Prediction", "Local Mapping", "Path Planning", "Simulation", "User Interface", "Embedded Implementation and Controls", "Signals Processing and Amplifier Design", "Vehicle Dynamics", "Sensor Mounting and Cooling", "Internal Affairs", "Marketing", "Finance", "Sponsorship", "Website", "Graphic Design"]
    n = ["Software","SensorFusion","Perception",
    "Prediction",    "Local",  "Path", "Simulation", "User", "Embedded", "Signals", "Vehicle", "SensorMount","Internal","Marketing","Finance", "Sponsorship", "Website","Graphic"]
    arrList = [Software, SensorFusion, Perception, Prediction, Local, Path, Simulation, User, Embedded, Signals, Vehicle, SensorMount, Internal, Marketing, Finance, Sponsorship, Website, Graphic]
    for i in range(0, len(f)):
        name = "Subteams/"+f[i]+"/" + n[i] + "Entries.csv"
        with open(name,'wb') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(arrList[i])

    name = "Subteams/All Entries" + "/AllEntries.csv"
    with open(name,'wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(s)

def addToList(a):
    b = [18, 20, 22, 24, 26, 28]
    # print("Rankings: \n ",a[18], a[20], a[22], a[24], a[26], a[28])
    for i in range(0, 6):
        if a[b[i]] == "Software Interface Management":
            # print"\nSoftware Detected!\n"
            Software.append(a)
        elif a[b[i]] == "Sensor Fusion":
            SensorFusion.append(a)
        elif a[b[i]] == "Perception":
            Perception.append(a)
        elif a[b[i]] == "Prediction":
            Prediction.append(a)
        elif a[b[i]] == "Local Mapping":
            Local.append(a)
        elif a[b[i]] == "Path Planning":
            Path.append(a)
        elif a[b[i]] == "Simulation":
            Simulation.append(a)
        elif a[b[i]] == "User Interface":
            User.append(a)
        elif a[b[i]] == "Embedded Implementation and Controls":
            Embedded.append(a)
        elif a[b[i]] == "Signals Processing and Amplifier Design":
            Signals.append(a)
        elif a[b[i]] == "Vehicle Dynamics":
            Vehicle.append(a)
        elif a[b[i]] == "Sensor Mounting and Cooling":
            SensorMount.append(a)
        elif a[b[i]] == "Internal Affairs":
            Internal.append(a)
        elif a[b[i]] == "Marketing":
            Marketing.append(a)
        elif a[b[i]] == "Finance":
            Finance.append(a)
        elif a[b[i]] == "Sponsorship":
            Sponsorship.append(a)
        elif a[b[i]] == "Website":
            Website.append(a)
        elif a[b[i]] == "Graphic":
            Graphic.append(a)


with open('entries.csv', 'rb') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # reader = csv.DictReader(csvfile)
    for row in readCSV:
        # print(x)
        # if x == 0:
        #     continue
        e.append([])


        #Applicant personal information
        e[x].append(row[1]) #firstname 1
        e[x].append(row[3]) #lastName 2
        e[x].append(row[5]) #email 3

        e[x].append(row[6]) #Program Terminal 4
        e[x].append(row[7]) #program 5
        e[x].append(row[8]) #Physically in Loo this term? (Y/N) 6
        e[x].append(row[9]) #In academic term? (Y/N) 7
        e[x].append(row[10]) #Previous affiliation with Wato 8

        #Position Interest
        e[x].append(row[11]) #Project Manager Commitment 9
        e[x].append(row[12]) #Subteam Lead Commitment 10
        e[x].append(row[13]) #Core Member Commitment 11
        e[x].append(row[14]) #PM interest 12
        e[x].append(row[15]) #SubLead Interest 13
        e[x].append(row[16]) #Core interest 14
        e[x].append(row[17]) #PM Software? 15
        e[x].append(row[18]) #PM Electrical? 16
        e[x].append(row[19]) #PM Mecanical? 17
        e[x].append(row[20]) #PM Business? 18
        # e[x].append("Subteam Lead Rankings")

        #Applicant rankings, Subteam Lead and Core Member
        if x == 0:
            e[x].append("Subteam Lead: SubTeam 1")
            e[x].append("Subteam Lead: Rank 1")
            e[x].append("Subteam Lead: SubTeam 2")
            e[x].append("Subteam Lead: Rank 2")
            e[x].append("Subteam Lead: SubTeam 3")
            e[x].append("Subteam Lead: Rank 3")

            e[x].append("Core Member: SubTeam 1")
            e[x].append("Core Member: Rank 1")
            e[x].append("Core Member: SubTeam 2")
            e[x].append("Core Member: Rank 2")
            e[x].append("Core Member: SubTeam 3")
            e[x].append("Core Member: Rank 3")
        else:
            e[x].append(row[21]) #19
            e[x].append(row[22])
            e[x].append(row[23])
            e[x].append(row[24])
            e[x].append(row[25])
            e[x].append(row[26]) #24
        # e[x].append("Core Member Rankings")
        # e[x].append([row[27], row[28], row[29], row[30], row[31], row[32]]) #CM team1
            e[x].append(row[27]) #25
            e[x].append(row[28])
            e[x].append(row[29])
            e[x].append(row[30])
            e[x].append(row[31])
            e[x].append(row[32]) #30

        #Applicant Essay and Resume
        e[x].append(row[33]) #Essay 1: Why Wato?
        e[x].append(row[34]) #Essay 2: Your qualification
        e[x].append(row[35]) #Resume Link

        #Survey Information
        e[x].append([row[36], row[37], row[38], row[39], row[40], row[41]]) #How did you hear about Wato?

        #Additional Information
        e[x].append(row[43]) #Additional comments
        e[x].append(row[45]) #EntryID #41



        x = x+1
        # print(row[1], row[3])
# e = [names_f, names_l]

Software.append(e[0])
SensorFusion.append(e[0])
Perception.append(e[0])
Prediction.append(e[0])
Local.append(e[0])
Path.append(e[0])
Simulation.append(e[0])
User.append(e[0])
Embedded.append(e[0])
Signals.append(e[0])
Vehicle.append(e[0])
SensorMount.append(e[0])
Internal.append(e[0])
Marketing.append(e[0])
Finance.append(e[0])
Sponsorship.append(e[0])
Website.append(e[0])
Graphic.append(e[0])



for i in range(0, x):
    addToList(e[i])


removeDupe(e)
writeCSV(e)

# print(e[1])
# print("\n\nSoftware!\n\n", Software)
# with open("Subteams/Software Interface Management/Entries.csv",'wb') as resultFile:
#     wr = csv.writer(resultFile, dialect='excel')
#     wr.writerows(Software)

for i in range(0, x):
    continue
