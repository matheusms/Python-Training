def do_twice(f, x):
    for i in range(x):
        f()

def print_spam():
    print('spam')

do_twice(print_spam,2)
