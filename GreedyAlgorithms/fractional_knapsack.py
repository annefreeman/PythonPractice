# Uses python3
import sys

# Task: The goal of this code probelm is to implement an algorithm for the fractional knapsack problem
# Input Format: The first line of the input contains the number n of items and the capacity W of a knapsack.
#               The next n lines define the values and weights of the items. 
#               The i-th line contains integers vi and Wi, the value and the weight of the i-th item, respectively
#        
# Output Format: Output the maximal value of fractions of items that fit into the knapsack. The absolute value of teh difference between the answer of your program
#                and the optimal value should be at most 10^-3. To ensure this, output your answer with at lease four digits after the decimal point



# Need to determine Values per weight --
# There exists an optimal solution that uses as much as possible of an item with the maximal value per unit of weight

def get_optimal_value(capacity, weights, values):
    value = 0
    for _ in range(0, len(weights)):
        if capacity == 0:
            return value
        
        #determine i with weight[i] > 0 and minimum value[i]/weight[i]
        i = 0
        findMinFractionalValue = 0
        for index in range (0, len(values)):
            if (weights[index] != 0 and values[index]/weights[index] > findMinFractionalValue):
                i = index 
                findMinFractionalValue = values[index]/weights[index]

        # determine the amount, it'll either be the weight of the object or the capacity
        amount = min(weights[i], capacity)
        # increment the value with the amount taken and the fractional weight
        value  = value + amount*(values[i]/weights[i])
        # update weight remaining of index to reflect amount taken
        weights[i] = weights[i]-amount
        # update capacity to reflect the amount taken
        capacity = capacity - amount

    return value


if __name__ == "__main__":
    #data = list(map(int, sys.stdin.read().split()))
    data = list(map(int,input("\nEnter the numbers : ").split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
