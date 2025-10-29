def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    #base cases
    if n==0:
        return 0
    if n==1:
        return 1
    #recursive step
    return fib_recursive(n-1, counts)+fib_recursive(n-2,counts)
    
    

    
def fib_top_down(n, fibs):
    #if the val has already been computed, return it
    if fibs[n] != -1:
        return fibs[n]
    #base cases
    if n==0:
        fibs[n]=0
        return 0
    if n==1:
        fibs[n]=1
        return 1
    #recursive step
    result= fib_top_down(n-1, fibs)+ fib_top_down(n-2, fibs)
    fibs[n]=result
    return result


def fib_bottom_up(n):
    #base cases
    if n==0:
        return 0
    if n==1:
        return 1
    
    #Initialize array to hold fib values
    fibs= [0]*(n+1)
    #set base cases
    fibs[0]=0
    fibs[1]=1
    #fill rest of array
    for i in range(2, n+1):
        fibs[i]=fibs[i-1]+fibs[i-2]
    return fibs[n]

