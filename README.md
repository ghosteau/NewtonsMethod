# Newton's Method
This is a Python file that can approximate the root of any function using Newton's method for approximating

This small project uses a cool mathematics library called SymPy, something I highly recommend checking out if you are into mathematics. 

As someone who has been getting more and more into calculus and mathematical programming, I thought it would be a fun little project to make a small algorithm that can find the zero of essentially any function by utilizing this awesome library.

How it works: Newton's method is iterative, so it was pretty natural how you could make this into a loop. What Newton's method actually does is takes an initial guess that you can choose, plugs it into your current function (we will use f(x)), and then divides it by f'(x) -- your derivative of the function. You simply subtract that from your guess, and then you will repeat this process, just using your brand new output value from the process above. I highly recommend checking out the formula if you are still confused, as it is technically an approximation technique, and not necessarily empirical (albeit, you can get VERY close to finding roots with lots of iterations). I recommend trying it yourself and seeing by inputting your own functions, and seeing how precise the guesses are in comparison to Desmos! Maybe I will eventually update it to be a full-fledged program with a prompt, but for now I just coded the functions and put an example of how to use it at the bottom.
