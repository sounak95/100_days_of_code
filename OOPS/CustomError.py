class ZeroDenominatorError(TypeError):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except TypeError:
    print('Type error occured')
except ZeroDivisionError:
    print('Zero Division Error occured')
except ZeroDenominatorError:
    print('Zero Denominator Error occured')
