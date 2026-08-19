def derivative(f, x, h=1e-5):
    """
    compute derivative
    """
    return (f(x + h) - f(x - h)) / (2 * h)


def function_value(function, value):
    """
    compute function at a value
    """
    return function(value)


def newtons_method(x0, function):
    """
    calculate function value and derivative value at current x, check if derivative is close to 0
    then calculate the next x, and check if the difference between the new x and old x is small, and
    then update the old x with the new x and repeat
    """
    while True:
        func_val = function_value(function, x0)
        derivative_calc = derivative(function, x0)

        if abs(derivative_calc) < 1e-9:
            print("too close to 0")
            break

        x_n1 = x0 - (func_val / derivative_calc)

        if abs(x_n1 - x0) < 1e-9:
            return x_n1
        x0 = x_n1
