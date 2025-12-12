// #OD42. GPU算力问题

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // GPU一次最多执行的任务数
    int onceNum;
    scanf("%d", &onceNum);

    // 任务数组长度
    int todoSize;
    scanf("%d", &todoSize);

    // 任务数组
    int todoArr[todoSize];
    int todoLast = 0;
    for (int i = 0; i < todoSize; i++) {
        scanf("%d", &todoArr[i]);
        // 计算所有任务数组元素入队，同时GPU处理后剩余的任务数
        // 上次剩余 + 本次入队 - 一次最大处理
        todoLast = (todoLast + todoArr[i] > onceNum) ? (todoLast + todoArr[i] - onceNum) : 0;
    }

    // 所有任务入队后，剩余的任务处理需要的时间 + 任务入队时间 = 总时间
    int time = todoSize;
    if (todoLast % onceNum != 0) {
        time += (todoLast / onceNum + 1);   // 无法整除，需要多处理一次
    } else {
        time += (todoLast / onceNum);
    }

    // 按要求输出
    printf("%d\n", time);
    return 0;
}
