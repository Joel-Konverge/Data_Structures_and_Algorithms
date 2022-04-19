def knapsack(weight,profit,capacity,n):
    #if capacity is full or n is on the first index return 0
    if capacity==0 or n==0:
        return 0
    #if weight of a particular index is greater than the capacity 
    if weight[n]>=capacity:
        #decrease the index by 1
        return knapsack(weight,profit,capacity,n-1)
    else:
        #
        return max(knapsack(weight,profit,capacity,n-1),profit[n]+knapsack(weight,profit,capacity-weight[n-1],n-1))
weight=[41, 50, 49, 59, 55, 57, 60]
profit =[442, 525, 511, 593, 546, 564, 617]

capacity=170
n=len(profit)-1
print(knapsack(weight,profit,capacity,n))



