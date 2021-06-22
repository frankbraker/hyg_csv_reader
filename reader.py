# the file 'hygfull.csv' comes from the following repository:
#
# https://github.com/astronexus/HYG-Database
#
# The version included here is probably out of date.
#
#

import csv

with open('hygfull.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            s = row[6]
            if len(s) == 0 or s[0]==" ":
                pass
            else:
                if s.isprintable():
                    # print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}.')
                    print(f'\tName = {row[6]},\tRA = {row[7]},\tDec = {row[8]},\tDistance = {row[9]},\tMagnitude = {row[10]},\t{row[11]}, {row[12]}, {row[13]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
