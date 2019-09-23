'''You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1'''

def coinChange(coins, amount):
    if amount<0:
            return -1
    coins=sorted(coins)
    d=[amount+1]*(amount+1)
    d[0]=0
    for i in range(amount+1):
        for j in coins:
            if j<=i:
                d[i]=min(d[i],d[i-j]+1)
            else:
                break
    return -1 if d[-1]>amount else d[-1]

print(coinChange([1,2,3,4,5], 17))