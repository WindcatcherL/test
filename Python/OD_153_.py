import sys

# 获取端口组长度，以及每个端口组（列表的列表）
M = int(input())
# 怎么获取每个端口组整理成列表的列表呢？ ---  **********
list_list = []
for _ in range(M):
    # 读取一行输入，并将字符串转为int型并去重
    list = sys.stdin.readline().strip()
    tmp = set(map(int, list.split(',')))
    list_list.append(tmp)

# print(list_list)





# 遍历list_list，对于当前list，如果后面的list有能合并的，就合并（新list再寻找其他list是否有能合并的） 
res = []
tag = [0]*(len(list_list))
for i in range(0, len(list_list)):
    
    # 遍历后面的list，检查是否能合并 ---> 如果后面的list能合并，怎么检查新list和别的list能否合并呢？并且再合并之后，怎么再检查呢？ --- **********
    # 代码问题+算法问题(以下代码画流程图较清晰)
    if tag[i] == 1:
        continue
    
    #获取当前列表，检查后面是否有能合并的
    now_list = list_list[i]
    for j in range(i+1, len(list_list)):
        #set集合交集、并集运算
        if len(now_list & list_list[j]) >= 2:
            now_list |= list_list[j]
            tag[j] = 1

    #检查now_list是否能合并到结果列表中,是则合并到这项中，否则创建一项（这个条件控制通过flag实现）
    flag = 0
    for k in range(len(res)):
        # res_temp = res[k]
        if len(now_list & res[k]) >= 2:
            res[k] |= now_list
            #条件控制
            flag = 1

    # 如果不能合并到结果列表某一项，新增一项
    if not flag:
        res.append(now_list)


# print(res)
#将结果列表转换格式输出
# result_str = '['
# for i in res:
#     result_str += '['
#     for j in i:
#         result_str += str(j) + ','
#     result_str = result_str[:-1]    #去掉最后一个元素
#     result_str += '],'
# result_str = result_str[:-1] + ']'
# print(result_str)





# =====================================以下是提交正确的格式============================================
# import sys

# def merge_port(list_list):
#     # 遍历list_list，对于当前list，如果后面的list有能合并的，就合并（新list再寻找其他list是否有能合并的） 
#     res = []
#     tag = [0]*(len(list_list))
#     for i in range(0, len(list_list)):
        
#         # 遍历后面的list，检查是否能合并 ---> 如果后面的list能合并，怎么检查新list和别的list能否合并呢？并且再合并之后，怎么再检查呢？ --- **********
#         # 代码问题+算法问题(以下代码画流程图较清晰)
#         if tag[i] == 1:
#             continue
        
#         #获取当前列表，检查后面是否有能合并的
#         now_list = list_list[i]
#         for j in range(i+1, len(list_list)):
#             #set集合交集、并集运算
#             if len(now_list & list_list[j]) >= 2:
#                 now_list |= list_list[j]
#                 tag[j] = 1

#         #检查now_list是否能合并到结果列表中,是则合并到这项中，否则创建一项（这个条件控制通过flag实现）
#         flag = 0
#         for k in range(len(res)):
#             # res_temp = res[k]
#             if len(now_list & res[k]) >= 2:
#                 res[k] |= now_list
#                 #条件控制
#                 flag = 1

#         # 如果不能合并到结果列表某一项，新增一项
#         if not flag:
#             res.append(now_list)

#     return res


# # 获取端口组长度，以及每个端口组（列表的列表）
# M = int(input())
# # 怎么获取每个端口组整理成列表的列表呢？ ---  **********

# if M < 1 or M > 10:
#     print([[]])
# else:
#     list_list = []
#     for _ in range(M):
#         # 读取一行输入，并将字符串转为int型并去重
#         list = sys.stdin.readline().strip()
#         tmp = set(map(int, list.split(',')))
#         list_list.append(tmp)

#     result = merge_port(list_list)
#     #按照格式print（int转str,列表元素用[和]）
#     result_str = '['
#     for x in result:
#         result_str += '['
#         for y in x:
#             result_str += str(y) + ','
#         result_str = result_str[:-1]
#         result_str += '],'
#     result_str = result_str[:-1] + ']'
#     print(result_str)



