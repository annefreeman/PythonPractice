# Uses python3
import sys
# want to get the last digit of the fibonacci number 
# can either calculate the number itself and then take the modulus 
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


# This version is pretty slow though, so we're better off just summing the remainders
# (234 + 567) % 10 = 4 % 10 + 7 % 10;
def get_fibonacci_last_digit_faster(n):
    #need to account for base case of zero
    if n <= 1:
        return n
    previous = 1
    current = 0
    for _ in range(2, n):
        temp = previous%10 + current%10
        current = previous%10
        previous = temp 
    return (previous + current)%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_faster(n))
