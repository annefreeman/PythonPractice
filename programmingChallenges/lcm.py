# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


#the product of gcd*lcm = the product of the two numbers
# eg. A= 15, B = 20, then gcd = 5 and LCM = 60
def lcm_faster(a,b):
    n1 = max(a,b)
    n2 = min(a,b)
    gcd = gcd_recursive(n1,n2)
    return ((a*b)/gcd)

def gcd_recursive(a,b):
    if b == 0:
        return a
    elif b == 1:
        return b
    a_prime = a%b
    return gcd_recursive(b, a_prime)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm_faster(a,b))

