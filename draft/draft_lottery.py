import itertools
import random


class Lottery:
    def __init__(self):
        self.team_odds = {
            "Nick": 16,
            "Mike": 15,
            "Chris": 14,
            "Jeff": 13,
            "Shawn": 11,
            "Pags": 9,
            "Conor": 8,
            "Andy": 6,
            "Matt": 5,
            "Drew": 4,
            "Ben": 3,
            "Tyler": 1
        }
        self.teams_in_lotto = {}
        self.combo_pool = []
        self.lotto_order = []
        self.manual = False

    def main(self):
        self.assign_combos()
        while self.teams_in_lotto:
            self.get_odds()
            if self.manual:
                self.irl_draw()
            else:
                self.auto_draw()

        self.print_odds()

    def irl_draw(self):
        self.print_odds()
        count = 1
        options, valid, choice = [], False, ''
        print
        print
        for team in self.team_odds:
            if count % 2 == 0:
                print '{} {}'.format('{}.'.format(count).ljust(3), team[0].ljust(12))
            else:
                print '{} {}|'.format('{}.'.format(count).ljust(3), team[0].ljust(12)),
            count += 1
            options.append(team)

        while not valid:
            try:
                if len(self.teams_in_lotto) % 2 != 0:
                    print
                choice = int(raw_input('\nWho was selected this round? > '))
                if 0 < choice <= len(options):
                    valid = True
                    choice = options[choice - 1]
                    chosen = [x for x in self.team_odds if choice == x][0]
                    self.lotto_order.append(chosen)

                    self.combo_pool = [x for x in self.combo_pool if x not in self.teams_in_lotto[chosen[0]]]
                    del self.teams_in_lotto[chosen[0]]
                    print
                else:
                    print 'Enter a number between 1 and {}'.format(len(options))
            except ValueError:
                print 'Enter a number between 1 and {}'.format(len(options))

    def auto_draw(self):
        pick = self.draw_numbers()
        for team, team_combos in self.teams_in_lotto.items():
            if pick in team_combos:
                pick = team
                chosen = [x for x in self.team_odds if pick == x[0]][0]
                self.lotto_order.append(chosen)
                break

        self.combo_pool = [x for x in self.combo_pool if x not in self.teams_in_lotto[pick]]
        del self.teams_in_lotto[pick]

    def print_odds(self):
        print
        print '{} | {} | {} | {}'.format('Rd'.rjust(3), 'Team'.ljust(5), 'Rd Odds'.rjust(6), 'Tot Odds')
        # print '{}{}'.format('Order'.ljust(20), 'Odds')
        print '-' * 32
        for i, v in enumerate(self.lotto_order):
            team = v[0]
            print '{} | {} | {}% |'.format(str((i + 1)).rjust(3), team.upper().ljust(5), str(v[1]).rjust(6))
            # print '{} {} {}%'.format('{}.'.format(i + 1).rjust(3), team.upper().ljust(7), str(v[1]).rjust(6))

        if len(self.team_odds) > 1:
            print
            print '{}{}'.format('Teams Left'.ljust(20), 'Chance')
            print '-' * 26

            for index, team in enumerate(self.team_odds):
                print '{} {}%'.format('{}.'.format((team[0] + ' ').upper().ljust(18, '.')), team[1])

    def get_odds(self):
        projected = []
        for team, combos in self.teams_in_lotto.items():
            odds = round(float(len(combos)) / float(len(self.combo_pool)) * 100, 1)
            projected.append((team, odds))

        projected.sort(key=self.get_key, reverse=True)
        self.team_odds = projected

    def assign_combos(self):
        tmp_combo_list = []
        for i in itertools.combinations(range(1, 16), 2):
            self.combo_pool.append(i)
            tmp_combo_list.append(i)

        for team, num_of_combos in self.team_odds.items():
            team = team.lower()
            for i in range(num_of_combos):
                if not self.teams_in_lotto.get(team):
                    self.teams_in_lotto[team] = []

                combo = random.choice(tmp_combo_list)
                self.teams_in_lotto[team].append(combo)
                tmp_combo_list.remove(combo)
                random.shuffle(tmp_combo_list)

    def draw_numbers(self):
        random.shuffle(self.combo_pool)
        combo = random.choice(self.combo_pool)
        return combo

    @staticmethod
    def get_key(item):
        return item[1]

if __name__ == '__main__':
    lotto = Lottery()
    lotto.main()
