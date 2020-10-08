# Uses python3
import sys

# Task: The goal in this code problem is to check whether an input sequence contains a majority element.
# Input: The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers
# Output: Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.


# Iterative Approach:
# create a dictionary with the elements and the counts from when they are seen
# Go through the dictionary values to see if any count > n/2 where n = length(array)
# if there is a value then return it, otherwise, return -1
# 
# Example Input 2 2 3 4 2
# Dictionary:
# 2 : 3
# 3 : 1
# 4 : 1
# In this case we would return 2 because it has count 3 which is > 5/2 = 2
def iterative_majority_elemnt(a):
    
    valCount = {}
    for element in a:
        if element in valCount.keys():
            valCount[element] += 1
        else:
            valCount[element] = 1

    requiredCount = int((len(a)/2))
    for search_count in valCount.values():
        if search_count > requiredCount:
            return valCount[search_count]
    return -1
# Recursive Approach: 
# if there exists a majority element in one of the half, 
# then it is not possible for any other element to be majority element in the overall array 
# because at least one half should have majority element. If not there doesn't exists any majority element.
def get_majority_element(a, left, right):
    if left == right:
        return a[int(left)]
    mid = int(left + ((right-left)/2))
    leftSideMajority = get_majority_element(a, left, mid)
    rightSideMajority = get_majority_element(a, mid+1, right)

    # count the halves and 
    # make sure the choosen majority is the majority in the half
    if leftSideMajority != -1:
        countLeft = 0
        for x in range(0, int((len(a)-1)/2)):
            if a[x] == leftSideMajority:
                countLeft = countLeft+1
        if countLeft > (int((len(a)-1)/2))/2:
            return leftSideMajority
    elif rightSideMajority != -1:
        countRight = 0
        for j in range(int((len(a)-1)/2)+1, len(a)-1):
            if a[j] == rightSideMajority:
                countRight = countRight+1
        if countRight > (int((len(a)-1)/2))/2:
            return rightSideMajority
    return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    n = int(input('please enter number: '))
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
