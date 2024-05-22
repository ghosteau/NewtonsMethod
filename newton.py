import sympy
from sympy import *
from sympy.calculus.util import continuous_domain

class NewtonUtil:

    @staticmethod
    def init_symbol(input_variable):
        if input_variable != str(input_variable):
            raise Exception("Must input string to initialize symbol")
        return symbols(input_variable)

    @staticmethod
    def init_function(input_function):
        if input_function != str(input_function):
            raise Exception("Must input string to initialize function")
        expression = sympify(input_function)
        return expression

    @staticmethod
    def domain(input_function):
        x = NewtonUtil.init_symbol("x")
        domain = continuous_domain(input_function, x, sympy.Reals)
        return domain

    @staticmethod
    def find_undefined(input_function):
        x = NewtonUtil.init_symbol("x")
        domain = continuous_domain(input_function, x, sympy.Reals)
        return Complement(sympy.Reals, domain)

    @staticmethod
    def newton_method(input_function, x0, iterations):
        x = NewtonUtil.init_symbol("x")
        function_prime = input_function.diff(x)

        if x0 not in NewtonUtil.domain(input_function):
            raise ValueError("x0 is not in the domain of the function; try another value")

        for iterate in range(iterations):
            evaluated_prime = function_prime.evalf(subs={x: x0})
            evaluated_function = input_function.evalf(subs={x: x0})

            if evaluated_prime == 0:
                raise ValueError("Evaluated prime was zero; try another value.")

            new_x = x0 - (evaluated_function / evaluated_prime)
            x0 = new_x

        return new_x


new_func = input("Input your function in terms of x -- be aware of how to write different operations: ")
new_func = NewtonUtil.init_function(new_func)
init_guess = input("What value would you like the algorithm to start with? (this is x-sub-zero): ")
init_iterations = input("How many iterations do you want to run? More iterations tend to be more accurate: ")

print("Approximated zero at: " + str(NewtonUtil.newton_method(new_func, float(init_guess), int(init_iterations))))
