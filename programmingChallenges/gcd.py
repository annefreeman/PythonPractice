# Uses python3
import sys
# GCD Problem
# For integers, a and b, their greatest common divisor or gcd(a, b) 
# is the largest integer d so that d divides both a and b
#
# Input: Integers a, b >= 0
# Output: gcd(a,b)


# Brute Force gcd
# find the max(current_gcd) between 2 and the lowest of a or b, 
# keeping in mind that a or b itself could be the gcd
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# Key Lemma:
# Let a' be the remainder when a is divided by b, then:
#          gcd(a,b) = gcd(a', b) = gcd(b,a')    
# Proof:
# a = a' + bq for some q
# d divides a and b if and only if it divides a' and b
def gcd_recursive(a,b):
    if b == 0:
        return a
    elif b == 1:
        return b
    a_prime = a%b
    return gcd_recursive(b, a_prime)

if __name__ == "__main__":
    a = int(input("Enter first integer for gcd:"))
    b = int(input("Enter second integer for gcd:"))
    n1 = max(a,b)
    n2 = min(a,b)
    print(gcd_naive(a, b))
    print(gcd_recursive(n1,n2))
