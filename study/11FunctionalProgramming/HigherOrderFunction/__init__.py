def my_abs(x: float = 1):
    print(x)
    return abs(x)


my_abs(-11)
my_abs(00)
my_abs(0o0100)
my_abs(3434)


# my_abs=100
# my_abs(3434)

def my_abs_v2(f, x: float = 1):
    if x < 0:
        print('alert')
    f(x)


my_abs_v2(my_abs, -11)
my_abs_v2(my_abs, 00)
my_abs_v2(my_abs, 0o0100)
my_abs_v2(my_abs, 3434)


def myabs_v3(x: float = 1):
    my_abs_v2(my_abs, x)
    myabs_v4()('****************')


def myabs_v4():
    return print


myabs_v3(-11)
myabs_v3(00)
myabs_v3(0o0100)
myabs_v3(3434)
