def jieti(n):

    # dp数组初始化，第n阶台阶，数组要有dp[n]
    dp = [0]*(n+1)

    # 阶梯问题中，dp[0]是没有意义的
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


# 获取输入，到达第n阶台阶
n = int(input())
result =jieti(n)
print(result)