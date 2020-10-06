# Uses python3
import sys

# Task: The goal in this problem is to find the minimum number of coins needed to change the input value (an integer)
#       into coins with denominations 1, 5, and 10
# Input: The input consists of a single integer m
# Constraints: 1 <= m <= 10^3
# Output: Output the minimum number of coins with the denominations 1,5, 10 that changes m
#
#  Examples
# Input: 28
# Ouptut: 6 (1+1)
# Explanation: 28 = 10 +10 + 5 + 1 + 1 + 1

def get_change(m):
    dimes = int(m/10)
    remainder = m-(dimes*10)
    nickels = int(remainder/5)
    remainder -= nickels*5

    return dimes+nickels+remainder

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input("Enter int value: "))
    print(get_change(m))
