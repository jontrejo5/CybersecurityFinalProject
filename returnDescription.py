import csv

def returnDescription(input):
    stringout = ''
    line_count=0
    with open('allitems.csv', 'r', errors='ignore') as csv_file:
        next(csv_file)
        next(csv_file)
        csv_read = csv.DictReader(csv_file)
        for row in csv_read:
 #           print (row)
            for entry in input:
                if entry in row["Description"]:
                    stringout += row["Description"]+"\n"
                    line_count += 1
    print(f'Returned {line_count} potential vulnerabilities.')
    if stringout == '':
        stringout = "\nNo Matches found"
    return stringout


 #   with open('allitems.csv', 'r') as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=',')
#        line_count = 0
#        for row in csv_reader:
#            if input[0] == row[2]:
#                 stringout += row[2]
#            line_count += 1
