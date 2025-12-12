def houzipashan(n):

    # 初始化数组
    dp = [0]*(n+1)

    # dp[0]没有意义
    # 每次1步或3步,赋值1、2、3阶，从4遍历
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    # range右不取
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    
    return dp[n]

n = int(input())
result = houzipashan(n)
print(result)

