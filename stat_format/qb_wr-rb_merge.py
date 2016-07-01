import os

qb_data = []
field_data = []

with open('QB/cleaned_weekly.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        qb_data.append(row)

with open('WR_RB/cleaned_weekly.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        field_data.append(row)

data = {x for x in qb_data for y in field_data if x['Name'] != y['Name']}
