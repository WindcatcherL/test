def feibonaqi(n):

    # 初始化dp数组
    dp = [0]*(n+1)

    # 斐波那契数列：f(0)=0, f(1)=1, ...
    dp[0] = 0
    dp[1] = 1

    # 递推式求每一项
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n = int(input())

result = feibonaqi(n)
print(result)
