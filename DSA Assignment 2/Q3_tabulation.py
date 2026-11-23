def fib_tab(n):
    dp = [0] * n

    if n > 1:
        dp[1]=1

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp
print(*fib_tab(10))