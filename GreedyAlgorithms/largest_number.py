#Uses python3

import sys

def get_larger(digit, maxDigit):
    results_greater = ""+str(digit)+str(maxDigit)
    results_maxIsGreater = ""+str(maxDigit)+str(digit)

    print("result_greater", results_greater)
    print("result maxIsGreater", results_maxIsGreater)
    if(int(results_greater) >= int(results_maxIsGreater)):
    	return bool(True) 
    return bool(False)
    
    


def largest_number(a):
    #write your code here
    result = ""
    for x in a:
        maxDigit = 0
        maxIndex = 0
        for digit in range(0,len(a)):
            if a[digit] != 0 and get_larger(a[digit],maxDigit):
                maxDigit = a[digit]
                maxIndex = digit
        result += str(maxDigit)
        print("result:", result)
        a[maxIndex] = 0
    return result

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = input.split()
    #a = data[1:]
    n = int(input("Enter numbers of numbers: "))
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
    print("list:", a)
    print(largest_number(a))
    
