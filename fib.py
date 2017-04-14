def fib(n):
    """A function to get the nth number in a fibronacci sequence
    
    :returns int"""

    if(n>1):
        return fib(n-1) + fib(n-2)
    elif (n==1):
        return 1
    else:
        return 0;

if __name__ == "__main__":
    print(fib(24))