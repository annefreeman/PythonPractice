# Uses python3

# fibonacci numbers: first element is 0, second is 1, 
#                    every number after is the sum of the previous two
# input = n
# output = the nth fibonacci number


# Recursive strategy to calculate the nth fibonacci number
def recursive_fib(n):
    if (n <= 1):
        return n

    return recursive_fib(n - 1) + recursive_fib(n - 2)


# iterative function call
# the recursive strategy is very repetitive and ends up calculting the same sum multiple times
# Since there is so much overlap in the recursive strategy, the iterative approach is better
def iterative_fib(n):
    #need to account for base case of zero
    if(n == 0):
        return n
    fib_n_1 = 1
    fib_n_2 = 0
    for i in range(2, n):
        temp = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = temp 
    return fib_n_1 + fib_n_2



         
# ask for input and call functions
if __name__ == "__main__":
    n = int(input())
    print("recursive:",recursive_fib(n))
    print("iterative:",iterative_fib(n))
