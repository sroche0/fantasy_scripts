__author__ = 'sroche'

players_in_draft = {}
draft_spot = {}


while players_in_draft:
    options, valid, choice = [], False, ''
    for key, value in enumerate(players_in_draft):
        print "%s. %s" % (key + 1, value)
        options.append(value)

    while not valid:
        try:
            choice = int(raw_input('\nWho was selected this round? > '))
            if 0 < choice <= len(options):
                valid = True
                choice = options[choice - 1]
            else:
                print 'That is not a valid choice. Enter a number between 1 and {}'.format(len(options))
        except ValueError:
            print 'That is not a valid choice. Enter a number between 1 and {}'.format(len(options))

    del players_in_draft[choice]

    probabilities, total = [], 0
    for key, value in players_in_draft.iteritems():
        total += len(value)
        prob = len(value) / total
        probabilities.append('{}|{}'.format(prob, key))

    print "Team     Probability"
    for i in sorted(probabilities):
        print "{}   -   {}".format(i)

    raw_input('Press any key when ready for next round')
