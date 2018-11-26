import csv

def returnDescription(input):

    stringout = ''

    with open('allitems.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if input[0] == row[2]:
                 stringout += row[2]
            line_count += 1
        print(f'Processed {line_count} lines.')

    if stringout == '':
        stringout = "\nNo data found"

    return stringout