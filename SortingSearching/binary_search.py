# Uses python3
import sys


# Task: The goal in this code problem is to implement the binary search algorithm.
# Input: The first line of the input contains an integer 𝑛 
#        and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct positive integers in increasing order. 
#        The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
# Output: For all 𝑖 from 0 to 𝑘−1, output an index 0≤𝑗≤𝑛−1 such that 𝑎𝑗 =𝑏𝑖 
#          or -1 if there is no such index.

def binary_search(A, low, high, key):
    if high < low:
        return -1
    middle = int(low + ((high-low)/2))
    if key == A[middle]:
        return middle
    elif key < A[middle]:
        return binary_search(A, low, middle-1, key)
    else:
        return binary_search(A, middle+1, high, key)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    # type in control + D to get this to work
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1] #raw data to search with
    a = data[1 : n + 1] #keys to search in/compare to
   
    for x in data[n + 2:]:
        print(binary_search(a, 0, len(a)-1, x), end = ' ')
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
