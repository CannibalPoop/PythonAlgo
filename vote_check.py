def vote_check(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote')

voted = {}
vote_check('Tom')
vote_check('Mike')
vote_check('Mike')