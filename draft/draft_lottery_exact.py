__author__ = 'sroche'
import itertools
import json
from collections import OrderedDict


def main():
    combo_pool = []
    with open('combos.json', 'rb') as f:
        combos_per_team = json.load(f)

    for k, v in combos_per_team.items():
        combo_pool.extend(v)

    nick, jeff, conor, ben, matt, shawn, john, andy, mike, chris, drew, pags = \
        '', '', '', '', '', '', '', '', '', '', '', ''
    teams = [[nick, 'nick'], [jeff, 'jeff'], [conor, 'conor'], [ben, 'ben'], [matt, 'matt'], [shawn, 'shawn'],
             [john, 'john'], [andy, 'andy'], [mike, 'mike'], [chris, 'chris'], [drew, 'drew'], [pags, 'pags']]
    results = {}
    for i in teams:
        i[0] = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 'name': i[1]}
        results[i[1]] = i[0]

    teams = [x[1] for x in teams]
    print teams
    # perms = itertools.permutations(teams)
    #
    # last = 0
    # for i, v in enumerate(perms):
    #     total = len(combo_pool)
    #     for index, value in enumerate(v):
    #         x_chance = float(len(combos_per_team[value])) / float(total) * 100
    #         results[value][index + 1].append(x_chance)
    #         total -= len(combos_per_team[value])
    #
    #     prog = int((float(i) / 479001600.00 * 100))
    #     if prog % 2 == 0 and prog != last:
    #         print '{}% done'.format(prog)
    #         last = int(prog)
    #
    # results_copy = dict(results)
    # for team, rounds in results_copy.items():
    #     for rnd, values in rounds.items():
    #         results[team][rnd] = sum(values) / len(values)
    #
    # for k, v in results.items():
    #     print "\n{}'s Results".format(k)
    #     print '-' * 15
    #     ordered = OrderedDict(sorted(v.items()))
    #     for key, value in ordered.iteritems():
    #         print "Round {} - {}%".format(key, value)

main()
