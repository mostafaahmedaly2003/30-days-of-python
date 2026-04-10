# Day 17 - Error Handling | SOLUTION
# Try to solve exercises.py yourself before looking here!

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'Error: cannot divide by zero'
    except TypeError:
        return 'Error: invalid types'
    else:
        return result
    finally:
        print('safe_divide called')
print(safe_divide(10, 2))
print(safe_divide(10, 0))
