import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-year', type=str, help='year to run on')
args = parser.parse_args()

# delimiter=',', quotechar='"'
with open('{} top 300.csv'.format(args.year), 'rb') as f:
    contents = csv.DictReader(f)
    player_ids, cleaned = [], []
    for row in contents:
        if not row['Player']:
            pass
        elif row['Player'] in ['Rk', 'Player']:
            pass
        else:
            row_copy = dict(row)
            first, last = row_copy['Player'].split(' ', 1)
            first = ''.join(e for e in first if e.isalnum())
            last = ''.join(e for e in last if e.isalnum())
            player_id = '{}{}{}'.format(first[:4].lower(), last[:4].lower(), row_copy['Pos'].lower())

            if player_id not in player_ids:
                player_ids.append(player_id)
            else:
                print 'Duplicate - {} - {} {}'.format(player_id, first, last)

            row_copy['PlayerID'] = player_id
            cleaned.append(row_copy)


with open('{}_player_ids.csv'.format(args.year), 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=row_copy.keys())
    writer.writeheader()
    writer.writerows(cleaned)
