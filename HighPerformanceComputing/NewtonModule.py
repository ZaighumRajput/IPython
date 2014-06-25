# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# A function that finds the root of a nonlinear function $f(x)$ 
# It uses Newton's Method: $$ x_{k+1}  = x_k - \frac{f(x_k)}{f^`(x_k)}$$ and requires and initial guess $x_0$

# <codecell>

def solve(fvals, x0, debug = False):
    iterator = 0
    deltaK = x0
    deltaK_plus1 = 0
    while(abs(fvals(deltaK)[0]) > 1e-14):
        
        
        deltaK_plus1 = deltaK - fvals(deltaK)[0]/fvals(deltaK)[1]
        iterator += 1    
        if __debug__:
            print "After %i iterations, x is %22.15e   " % (iterator, deltaK_plus1)
        
        
        deltaK = deltaK_plus1
        
        
        if(iterator > 20):
            break
        
    return  deltaK, iterator

# <headingcell level=4>

# Test Cases:

# <codecell>

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=True):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x

# <codecell>

test1()

# <codecell>

a[1]

# <codecell>


