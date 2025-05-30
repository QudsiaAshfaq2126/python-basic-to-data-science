
def check_non_negative_integer(f):
    def wrapper(n):
        if isinstance(n, int) and n >= 0:
            return f(n)
        else:
            raise Exception("Input must be a non-negative integer")
    return wrapper
@check_non_negative_integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
try:
    print("factorial(1.354):", factorial(1.354))
except Exception as e:
    print("Error:", e)

try:
    print("factorial(-1):", factorial(-1))
except Exception as e:
    print("Error:", e)

print("factorial(5):", factorial(5))

