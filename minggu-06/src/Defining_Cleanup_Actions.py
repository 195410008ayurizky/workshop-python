try:
    raise KeyboardInterrupt
finally:
     print('Goodbye, world!')
#output
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>

def bool_return():
     try:
         return True
     finally:
         return False
bool_return()
#output
False

def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

divide(2, 1)
#output
result is 2.0
executing finally clause

divide(2, 0)
#output
division by zero!
executing finally clause

divide("2", "1")
#output
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'