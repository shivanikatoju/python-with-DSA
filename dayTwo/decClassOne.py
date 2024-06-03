'''
A simple class Decorator
'''

class Decorator:
    def __init__(self, fun):
        self.func = fun 

    def __call__(self):
        print(f'----------------call method ------------------')
        self.func()
        print('***********************************************')

def fun():
    print('fun() called')

fun = Decorator(fun) # __init__(fun)  is called 
fun() # __call__() is called