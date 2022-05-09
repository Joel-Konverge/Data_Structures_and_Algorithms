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
print(knapsack_dp(weight,profit,capacity,n,dp))
