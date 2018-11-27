import csv

def returnDescription(input):

    stringout = ''

    with open('allitems.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for item in input:
                if item == row[2]:
                    stringout += "\n" + str(row[2]) + "\n"
                line_count += 1
                
    if stringout == '':
        stringout = "\nNo data found"

    return stringout