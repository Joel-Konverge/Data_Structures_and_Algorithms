def knapsack(weight,profit,capacity,n):
    #if capacity is full or n is on the first index return 0
    if capacity==0 or n==0:
        return 0
    #if weight of a particular index is greater than the capacity 
    if weight[n]>=capacity:
        #decrease the index by 1
        return knapsack(weight,profit,capacity,n-1)
    else:
        # return max out of two cases:if included it gives the adds the profit and deducts the capacity , if excluded deducts the index
        return max(knapsack(weight,profit,capacity,n-1),profit[n]+knapsack(weight,profit,capacity-weight[n-1],n-1))
weight=[41, 50, 49, 59, 55, 57, 60]
profit =[442, 525, 511, 593, 546, 564, 617]

capacity=170
n=len(profit)-1
print(knapsack(weight,profit,capacity,n))


#using DP

def knapsack_dp(weight,profit,capacity,n,dp):
    if capacity==0 or n==0:
        return 0
    if dp[n][capacity] is not None:
        return dp[n][capacity]
    if weight[n-1]<=capacity:
        dp[n][capacity]=max(knapsack_dp(weight,profit,capacity,n-1,dp),profit[n-1]+knapsack_dp(weight,profit,capacity-weight[n-1],n-1,dp))
        return dp[n][capacity]
    else:
        dp[n][capacity]=knapsack_dp(weight,profit,capacity,n-1,dp)
        return dp[n][capacity]

weight=[41, 50, 49, 59, 55, 57, 60]
profit =[442, 525, 511, 593, 546, 564, 617]

capacity=170
n=len(profit)

dp=[[None]*(capacity+1) for _ in range(n+1)]
# print(dp)
print(knapsack_dp(weight,profit,capacity,n,dp))


def kProfit(W,N,wt,pr,dp):
    # Base Condition
    if N==0 or W==0:
        return 0
    # If sub problem is previously solved tehn return it.
    if dp[N][W] is not None:
        return dp[N][W]
    if wt[N-1] <= W:
        dp[N][W] = max(pr[N-1]+kProfit(W-wt[N-1],N-1,wt,pr,dp), kProfit(W,N-1,wt,pr,dp))
        return dp[N][W]
    else:
        dp[N][W] = kProfit(W,N-1,wt,pr,dp)
        return dp[N][W]
if __name__ == '__main__':
    W = 170
    wt = [41, 50, 49, 59, 55, 57, 60]
    pr = [442, 525, 511, 593, 546, 564, 617]
    N = len(pr)
    # define DP array
    dp = [[None] * (W + 1) for _ in range(N + 1)]
    # Call for kProfit to calculate max profit
    maxProfit = kProfit(W,N,wt,pr,dp)
    print('Maximum Profit is : ',maxProfit)