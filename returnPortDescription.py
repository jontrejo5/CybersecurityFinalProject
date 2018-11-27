
import csv

def returnPortDescription(portNum):
    with open("service-names-port-numbers (1).csv", mode = 'r') as f:
        csvDict=csv.DictReader(f)
        for row in csvDict:
            workNums=row["Port Number"].split("-")
            if len(workNums) <2:
                if portNum == int(row["Port Number"]):
                    return row["Description"]
            else:
                if int(workNums[0]) <= portNum <= int(workNums[1]):
                    return row["Description"]
#            workLine = line.split(",")
#            if len(workLine) >=3:
#                if workLine[1] == portNum:
#                    writeline = workLine[3]
#                    return writeline
#            else:
#                portRange = workLine[0].split("-")
#                if portNum >= int(portRange[0]) and portNum <= int(portRange[1]):
#                    return workLine[1]

    f.close()