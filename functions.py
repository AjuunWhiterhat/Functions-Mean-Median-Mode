import csv 
from collections import Counter

with open("HeightWeight2.csv",newline="") as f:
    Reader = csv.reader(f)
    fileData = list(Reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))


n = len(newData)

newData.sort()

def mean():
    total = 0
    for x in newData:
        total += x
        mean = total / n

    print("Mean (Average) is : "+str(mean))


def median():
    newData.sort()
    if n%2==0:
        median1 = float(newData[n//2])
        median2 = float(newData[n//2-1])
        median = (median1 + median2)/2

    else:
        median = float(newData[n//2])
        print(n)

    print("Median is : "+str(median))

def mode():
    data = Counter(newData)
    modDataforRange = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
    }

    for weight,frequency in data.items():
        if 75<float(weight)<85:
            modDataforRange["75-85"]+=frequency
        elif 85<float(weight)<95:
            modDataforRange["85-95"]+=frequency
        elif 95<float(weight)<105:
            modDataforRange["95-105"]+=frequency
        elif 105<float(weight)<115:
            modDataforRange["105-115"]+=frequency
        elif 115<float(weight)<125:
            modDataforRange["115-125"]+=frequency
        elif 125<float(weight)<135:
            modDataforRange["125-135"]+=frequency
        elif 135<float(weight)<145:
            modDataforRange["135-145"]+=frequency
        elif 145<float(weight)<155:
            modDataforRange["145-155"]+=frequency
        

    modRange,modFrequency = 0,0

    for range,occ in modDataforRange.items():
        if frequency>occ:
            modRange,modFrequency = [int(range.split("-")[0]),int(range.split("-")[1])],occ

    mod = float((modRange[0]+modRange[1])//2)

    print(f"Mode is : {mod:2f}")

mean()
median()
mode()

