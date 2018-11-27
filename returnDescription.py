import csv

def returnDescription(input):
    listOut=[]
    stringout=''
    URL=''
    line_count=0
    with open('allitems.csv', 'r', errors='ignore') as csv_file:
        next(csv_file)
        next(csv_file)
        csv_read = csv.DictReader(csv_file)
        for row in csv_read:
 #           print (row)
            for entry in input:
                if entry in row["Description"]:
                    getURL=row["References"].split("|")
                    for refs in getURL:
                        if "URL:" in refs:
                            URL=refs[7:-3]
                    listOut.append(row["Name"] +", " + row["Description"]+", "+URL)
                    line_count += 1
    stringout ="Returned " + str(line_count) + " potential vulnerabilities."
    if line_count == 0:
        stringout = "No Matches found"
    return stringout, listOut
