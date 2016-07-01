import csv
import os

cwd = os.getcwd()
for (dirpath, dirnames, filenames) in os.walk(cwd):
    csv_files = [x for x in filenames if 'cleaned' not in x and '.csv' in x]

cleaned = []
if 'QB' in dirpath:
    fieldnames = ["Rk", "Name", "Age", "Date", "Lg", "Tm", "", "Opp", "Result",
                  "G#", "Week", "Day", "Cmp", "PaAtt", "Cmp%", "PaYds", "PaTD", "Int", "Rate",
                  "Y/A", "AY/A", "RuAtt", "RuYds", "Y/A", "RuTD", "Tgt", "Rec", "RecYds",
                  "Y/R", "RecTD", "XPM", "XPA", "XP%", "FGM", "FGA", "FG%", "2PM", "Sfty",
                  "Pts", "Touch", "TotOff", "YdsScm", "APYd", "RtY"]
elif 'WR_RB' in dirpath:
    fieldnames = ['Rk', 'Name', 'Age', 'Date', 'Lg', 'Tm', '', 'Opp', 'Result',
                  'G#', 'Week', 'Day', 'RuAtt', 'RuYds', 'Y/A', 'RuTD', 'Tgt', 'Rec', 'RecYds',
                  'Y/R', 'RecTD', 'XPM', 'XPA', 'XP%', 'FGM', 'FGA', 'FG%', '2PM', 'Sfty', 'Pts',
                  'Touch', 'TotOff', 'YdsScm', 'APYd', 'RtY']

to_remove = ["Age", "Lg", "Day", "XPM", "XPA", "XP%", "FGM", "FGA", "FG%",
             "PM", "Sfty", "RtY", "APYd"]

for i in csv_files:
    with open(i, 'rb') as f:
        contents = csv.reader(f, delimiter=',', quotechar='"')
        for row in contents:
            try:
                if not row[0]:
                    pass
                elif row[0] == 'Rk':
                    pass
                else:
                    # first, last = row[1].split(' ')
                    # first = ''.join(e for e in row[1] if e.isalnum())
                    # last = ''.join(e for e in row[1] if e.isalnum())
                    # first, last = row[1].split(' ', 1)
                    # row.insert(2, argv[1][6:10])
                    # player_id = '{}{}'.format(first[:4].lower(), last[:4].lower(),
                    #                             row[20].lower())
                    # del row[22:]
                    row_copy = list(row)
                    for index, value in enumerate(row):
                        if value in [0, '0']:
                            row_copy[index] = ''

                    clean_row = dict(zip(fieldnames, row_copy))

                    for item in to_remove:
                        try:
                            del clean_row[item]
                        except KeyError:
                            pass

                    cleaned.append(clean_row)
            except IndexError:
                pass

fieldnames = [x for x in fieldnames if x not in to_remove]

with open('cleaned_weekly.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"')
    writer.writeheader()
    writer.writerows(cleaned)
