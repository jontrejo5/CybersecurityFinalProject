def returnDescription(input):
    cve=open("allitems.txt", "r")
    for word in input:
        for entry in cve.split("======================================================"):
            if word in entry:
                print (entry)
                return entry
