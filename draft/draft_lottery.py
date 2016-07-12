import json


def main():
    # Open the json with the assigned ball combos for the teams. This is generated ahead of time by another script
    with open('combos.json', 'rb') as f:
        players_in_draft = json.load(f)

    # Combines all the possible combinations into a pool to be referenced by the random number selection
    combo_pool, lotto_order = [], []
    for key, combos in players_in_draft.items():
        combo_pool.extend(combos)

    while players_in_draft:
        odds = print_odds(players_in_draft, combo_pool, lotto_order)

        count = 1
        options, valid, choice = [], False, ''
        print
        print
        for team, combos in players_in_draft.items():
            if count % 2 == 0:
                print '{} {}'.format('{}.'.format(count).ljust(3), team.ljust(12))
            else:
                print '{} {}|'.format('{}.'.format(count).ljust(3), team.ljust(12)),
            count += 1
            options.append(team)

        while not valid:
            try:
                if len(players_in_draft) % 2 != 0:
                    print
                choice = int(raw_input('\nWho was selected this round? > '))
                if 0 < choice <= len(options):
                    valid = True
                    choice = options[choice - 1]
                    odds = [x[1] for x in odds if choice in x]
                    lotto_order.append((choice, odds[0]))
                    combo_pool = [x for x in combo_pool if x not in players_in_draft[choice]]
                else:
                    print 'Enter a number between 1 and {}'.format(len(options))
            except ValueError:
                print 'Enter a number between 1 and {}'.format(len(options))

        del players_in_draft[choice]
        print


def print_odds(teams_left, combo_pool, lotto_order):
    print
    print '{}{}'.format('Order'.ljust(20), 'Odds')
    print '-' * 26
    for i, v in enumerate(lotto_order):
        print '{}{}{}%'.format('{}.'.format(i + 1).ljust(3), v[0].upper().ljust(17), v[1])

    print
    print '{}{}'.format('Teams Left'.ljust(20), 'Chance')
    print '-' * 26
    projected = []
    for team, combos in teams_left.items():
        odds = round(float(len(combos)) / float(len(combo_pool)) * 100, 2)
        projected.append((team, odds))

    projected.sort(key=get_key, reverse=True)
    for index, team in enumerate(projected):
        print '{} {}%'.format('{}.'.format((team[0] + ' ').upper().ljust(18, '.')), team[1])

    return projected


def get_key(item):
    return item[1]

if __name__ == '__main__':
    main()
