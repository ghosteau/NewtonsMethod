import sympy
from sympy import *
from sympy.calculus.util import continuous_domain

def init_symbol(input_variable):
    if input_variable != str(input_variable):
        raise Exception("Must input string to initialize symbol")
    return symbols(input_variable)

def init_function(input_function):
    if input_function != str(input_function):
        raise Exception("Must input string to initialize function")
    expression = sympify(input_function)
    return expression

def domain(input_function):
    x = init_symbol("x")
    domain = continuous_domain(input_function, x, sympy.Reals)
    return domain

def find_undefined(input_function):
    x = init_symbol("x")
    domain = continuous_domain(input_function, x, sympy.Reals)
    return Complement(sympy.Reals, domain)

def newton_method(input_function, x0, iterations):
    x = init_symbol("x")
    function_prime = input_function.diff(x)

    if x0 not in domain(input_function):
        x0 = input("X0 was not in the domain, try another value: ")
        x0 = float(x0)

    for iterate in range(iterations):
        evaluated_prime = function_prime.evalf(subs={x: x0})
        evaluated_function = input_function.evalf(subs={x: x0})

        if evaluated_prime == 0:
            raise ValueError("Evaluated prime was zero; try another value.")

        new_x = x0 - (evaluated_function / evaluated_prime)
        x0 = new_x

    return new_x


new_func = input("Input your function in terms of x -- be aware of how to write different operations: ")
new_func = init_function(new_func)
init_guess = input("What value would you like the algorithm to start with? (this is x-sub-zero): ")
init_iterations = input("How many iterations do you want to run? More iterations tend to be more accurate: ")

print("Approximated zero at: " + str(newton_method(new_func, float(init_guess), int(init_iterations))))
