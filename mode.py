import csv
from collections import Counter

file = open("124.csv", newline = "")
reader = csv.reader(file)

filedata = list(reader)
filedata.pop(0)


newdata = []
for i in range(len(filedata)):
    number = filedata[i][2]
    newdata.append(float(number))

data = Counter(newdata)
rangedata = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if(50<float(height)<60):
        rangedata["50-60"]+=occurence 
    elif(60<float(height)<70):
        rangedata["60-70"]+=occurence
    elif(70<float(height)<80):
        rangedata["70-80"]+=occurence

moderange,modeoccurence = 0,0
for range,occurence in rangedata.items():
    if(occurence>modeoccurence):
        moderange,modeoccurence = [int(range.split("-")[0]), int(range.split("-")[1])],occurence

mode = float((moderange[0]+moderange[1])/2)

print(mode)
