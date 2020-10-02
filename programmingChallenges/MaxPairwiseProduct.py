# python3

# input: the number of integers in the sequence (n)
# second input: the sequence of n non-negative integers
# output: the largest integer that can be obtained by multiplying two elements in the sequence
# Note: elements may not be unique


# brute force approach
# in the brute force approach we go through the array twice and 
# multiply the number we are checking against the other numbers in the array
# we track a max product
def bruteforce_max_pairwise_product(numbers):
    max_product = 0
    for first in range(len(numbers)):
        for second in range(first + 1, len(numbers)):
            if(max_product < numbers[first] * numbers[second]):
                max_product = numbers[first] * numbers[second]
    return max_product


# Observation: the maximum product of a sequence will be the product of 
#              the two largest numbers
# not gaurenteed a unique sequence of numbers, use boolean to track if largest is found
def cleaner_max_pairwise_product(numbers):
    largest = 0
    second_largest = 0
    found = False 
    for n in numbers:
        if n > largest:
            largest = n

    for n in numbers:
        if n == largest and found == False:
            found = True
            continue
        elif n > second_largest:
            second_largest = n

    return second_largest*largest


# Try to do it in a single loop
# challenging to set the correct starting conditions because should work with list as small as two elements
# Decided to compare the value of first number with next number to set the value of second_largest 
def singleloop_max_pairwise_product(numbers):
    largest = None
    second_largest = None
    for n in numbers:
        #this if statement only runs for the first iteration
        if largest is None:
            largest = n
            second_largest = min(numbers[0], numbers[1])
            continue

        # check if current value is greater than largest
        # then set the second_largest to the current largest
        # and the largest to the latest viewed largest
        if n > largest:
            second_largest = largest
            largest = n

        #otherwise, see if the current value is larger than the second largest
        # and less than or equal to the largest value
        # the second_largest and largest could be equal because duplicates
        elif n > second_largest and n <= largest:
            second_largest = n
    return largest*second_largest

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(bruteforce_max_pairwise_product(input_numbers))
    print(cleaner_max_pairwise_product(input_numbers))
    print(singleloop_max_pairwise_product(input_numbers))
