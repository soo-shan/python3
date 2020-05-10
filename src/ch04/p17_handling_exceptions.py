def no_return():
    print(" I'm about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

# Catch all exceptions
try:
    no_return()
except:
    print("I caught an exception")
print("executed after the exception")

# Catch  specific exception
def funny_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"

print(funny_division(0))
print(funny_division(50.0))
print(funny_division("Hello"))

# Catch more than one exception
def funny_division2(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100/divider
    except (ZeroDivisionError, TypeError):
        return "You either entered Zero or a string.\nPlease enter a valid number."

for val in (0, "hello", 50.0, 13):
    print(f"Testing : {val} >>", end=" ")
    print(funny_division2(val),"\n")

# Catch multiple exceptions and perform different operations with them
def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number.")
        return 100/divider
    except ZeroDivisionError:
        return "Enter a number other than Zero."
    except TypeError:
        return "Enter a numerical value."
    except ValueError:
        print("No, No, not 13!")
        raise #this re-raises the ValueError exception again

for val in (0, "hello", 50.0, 13):
    print(f"Testing : {val} >>", end=" ")
    print(funny_division3(val),"\n")

# Capture an exception as a variable
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)

# Execute code only if an exception does not occur
import random
some_exceptions = [ValueError, TypeError, IndexError, None]
try:
    choice = random.choice(some_exceptions)
    print("Raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" %(e.__class__.__name__))
else:
    print("This code is called if there is no exception")
finally:
    print("This cleanup code is always called")
