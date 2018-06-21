def make_greeting(user_id):
    return 'hello, user' + user_id

def print_greeting(i):
    print(make_greeting(i))
    
print_greeting(0)
print_greeting(3.0)
print_greenting([1,2,3])
