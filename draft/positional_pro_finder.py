__author__ = 'sroche'
from collections import OrderedDict
import csv
import requests
import random
import json

ITERATIONS = 10000000


def main():
    combo_pool = []
    with open('combos.json', 'rb') as f:
        combos_per_team = json.load(f)

    for k, v in combos_per_team.items():
        combo_pool.extend(v)

    with open('random.txt', 'rb') as f:
        random_num_pool = list(f.read().split())

    nick, jeff, conor, ben, matt, shawn, john, andy, mike, chris, drew, pags = \
        '', '', '', '', '', '', '', '', '', '', '', ''
    teams = [[nick, 'nick'], [jeff, 'jeff'], [conor, 'conor'], [ben, 'ben'], [matt, 'matt'], [shawn, 'shawn'],
             [john, 'john'], [andy, 'andy'], [mike, 'mike'], [chris, 'chris'], [drew, 'drew'], [pags, 'pags']]
    results = {}
    for i in teams:
        i[0] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 'name': i[1]}
        results[i[1]] = i[0]

    nums, progress = [], 0
    for x in range(1, ITERATIONS + 1):
        players_in_draft = dict(combos_per_team)
        for i in range(1, 12):
            valid = False
            while not valid:
                empty_teams = 0
                if empty_teams >= 12:
                    exit("Teams Didn't Refresh")
                if not nums:
                    random.shuffle(random_num_pool)
                    nums = list(random_num_pool)
                    # r = requests.get("https://www.random.org/integers/?num=10000&min=0&max=104&col=100&base=10&"
                    #                  "format=plain&rnd=new")
                    # with open('random.txt', 'ab') as f:
                    #     f.write(r.text)
                    # nums = list(r.text.split())

                draw = combo_pool[int(nums.pop())]
                for k, v in players_in_draft.iteritems():
                    if v:
                        if draw in v:
                            valid = True
                            results[k][i] += 1
                            players_in_draft[k] = []
                            delete = k
                    else:
                        empty_teams += 1

                if valid:
                    del players_in_draft[delete]
            else:
                pass
        last, val = players_in_draft.items()[0]
        results[last][12] += 1
        progress_bar(progress, x, ITERATIONS)
        progress = int(float(x) / float(ITERATIONS) * 100)

    writable_results = []

    with open('output.csv', 'wb') as f:
        fieldnames = ['name', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(writable_results)

    for team, results in results.items():
        writable_results.append(results)

        # for k, v in results.items():
        #     print "\n{}'s Results".format(k)
        #     print '-' * 15
        #     ordered = OrderedDict(sorted(v.items()))
        #     for key, value in ordered.iteritems():
        #         try:
        #             tot = float(value)
        #             pct = tot / float(ITERATIONS) * 100
        #             print "Round {} - {}%".format(key, pct)
        #         except ValueError:
        #             pass


def progress_bar(last, current, total):
    if last != int(float(current) / float(total) * 100):
        pct_done = int(float(current) / float(total) * 100)
        complete = int(float(current) / float(total) * 73)
        left = 73 - complete
        print '[{}{}]{}{}%'.format('#' * complete, '.' * left, ' ' * (4 - len(str(pct_done))), pct_done)


if __name__ == '__main__':
    main()
