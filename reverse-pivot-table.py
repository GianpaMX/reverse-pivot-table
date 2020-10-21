import csv
import fileinput

columns = []
len_columns = 0

with fileinput.input() as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_index = 0
    col_index = 0
    for row in csv_reader:
        if row_index == 0:
            columns = row.copy()
            len_columns = len(columns)
        else:
            for cell in row:
                if col_index != 0:
                    print(row[0], end=', ')
                    print(cell, end=', ')
                    if col_index < len_columns:
                        print(columns[col_index])
                    else:
                        print()
                col_index += 1
            col_index = 0
        row_index += 1
