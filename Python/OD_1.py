# 数组长度
N = int(input())

# 数组值
arr = list(map(int, input().split()))

# 窗口大小
M = int(input())

# 获取前M个元素之和
windows_sum = sum(arr[:M])
max_sum = windows_sum

# 从索引M遍历数组，每次减去索引i-M，加上i
for i in range(M, N):
    windows_sum = windows_sum - arr[i-M] + arr[i]
    max_sum = max(max_sum, windows_sum)

print(max_sum)



#后续git提交