def make_greeting(user_id):
    return 'hello, user' + user_id

def print_greeting():
    print(make_greeting(0))
    print(make_greeting(1.1))
