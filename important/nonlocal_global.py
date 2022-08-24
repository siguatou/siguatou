x = 10

def func():
    # x = 10000
    def inner_func():
        # nonlocal x
        # global x
        # x += 1
        y = x * 2
        print(x)
        print(y)
    return inner_func

func()()