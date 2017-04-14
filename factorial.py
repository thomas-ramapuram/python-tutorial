def factorial(n):
    """A function to calculate the factorial of a number
    
    :return int"""

    if(n > 1):
        return n * factorial(n-1);
    else:
        return 1


if __name__ == "__main__":
    print(factorial(10))