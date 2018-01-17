def my_method(arg1, arg2):
    return arg1+arg2


my_method(5,6)

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(5, 6, 7, 3, 5, 1)

my_list_addition([5, 6, 7, 3, 5, 1])

def addition_simplified(*args):  #list of args
    return sum(args)

addition_simplified(5, 6, 7, 3, 5, 1)


##

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 54, 12, 22, name='Ahmed', location='NO')
