# python3
import sys

# Problem: You are going to travel to another city that is located d miles away from your home city. Your car can travel
# at most m miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, ..., stopn
# from your home city. What is the minimum number of refills needed?

# Input: The first line contains an integer d (distance from home city to location). 
# The second line contains an integer m (miles you can drive on full tank). 
# The third lines specifies an integer n (number of gas stations)
# Finally, The last line contains integers stop1, stop2, ..., stopn


# I have selected the greedy choice of refilling at the farthest reachable gas station
def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills = 0
    currentRefill = 0
    lastRefill = 0
    while (currentRefill < len(stops)-1):
        print("currentRefill Index:",currentRefill)
        print("Refill location:",stops[currentRefill])
        lastRefill = currentRefill
        # go through the array of stops
        # determine if we can travel the distance to the next refill stop
        # if we can then increment the currentRefill position counter
        while(currentRefill < (len(stops)-1) and (stops[currentRefill+1]-stops[lastRefill] <= tank) ):
            currentRefill = currentRefill+1
        #if the currentRefill spot is the same as the lastRefill than we cannot advance and the journey is impossible
        if currentRefill == lastRefill:
            return -1
        # if we stopped for a refill before the end of the array, then increment the numRefilles counter
        if currentRefill <= len(stops):
            numRefills = numRefills+1
    return numRefills

if __name__ == '__main__':
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    d = int(input("Enter distance to destination: "))
    m = int(input("Enter miles on full tank: "))
    n = int(input("Enter number of gas stations: "))
    stops = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
    # add the destination as a stop
    stops.append(d)
    print(compute_min_refills(d, m, stops))
