def newtonRalphson(g,x0,eps,delta,itermax):
#SANASISI_PP9 Function implements the Newton Ralphsons method to solve a function g(x)
#provided initial guess of x0
#
#   Inputs:
#       g - Non linear Function given to be solved
#       x0 - Initial guess for the solution 
#       eps - Tolerance for convergence criteria decimal
#       delta - Threshold for divergence criteria decimal
#       itermax - Maximum number of iterations integer
# 
#   Outputs:
#       x - Solution decimal
#       iter - Number of iterations taken to reach the solution number

    x = x0
    i = 0#Initial iteration variable to 0
    while i<itermax:
        f,fx = g(x)#Evaluate the function and its derivative at x0 intitial guess
        if abs(f)<eps:#Loop will break automatically when convergence occured else raise errror
            return x,i
        x_next = x-(f/fx)#Next iteration
        if abs(x_next-x)>delta:#Check for divergence
            raise ValueError('Error: Divergence')
        x=x_next#Update current iteration
        i+=1#Update iteration
    raise ValueError('Error: Maximum Iteratons reached')        
