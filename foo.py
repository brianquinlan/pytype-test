import itertools

def make_greeting(user_id):
    return 'hello, user' + user_id

def print_greeting():
    print(make_greeting(123))

itertools.chain(1,2,3) + itertools.chain('abc')
