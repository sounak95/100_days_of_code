
# https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def func1(day, last, points):
    if day==0:
        max_i=0
        for task in range(0, 3):
            if task!=last:
                max_i = max(max_i, points[0][task])
        return max_i

    max_i=0
    for task in range(0, 3):
        if task != last:
            point = points[day][task] + func(day-1, task, points)
            max_i = max(max_i, point)
    return max_i


def ninjaTraining1(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    return func1(n-1, 3, points)




def func2(day, last, points,dp):
    if day==0:
        max_i=0
        for task in range(0, 3):
            if task!=last:
                max_i = max(max_i, points[0][task])
        return max_i

    if dp[day][last]!=-1:
        return dp[day][last]
    max_i=0
    for task in range(0, 3):
        if task != last:
            point = points[day][task] + func2(day-1, task, points, dp)
            max_i = max(max_i, point)
    dp[day][last]=max_i
    return dp[day][last]


import copy
def ninjaTraining2(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    dp = []
    l1 = [-1] * 4
    for i in range(n):
        dp.append(copy.deepcopy(l1))

    return func2(n-1, 3, points, dp)


def ninjaTraining3(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    dp = []
    l1 = [-1] * 4
    for i in range(n):
        dp.append(copy.deepcopy(l1))

    dp[0][0]= max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(0,4):
            dp[day][last] =0
            for task in range(0,3):
                if task!=last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], point)

    return dp[n-1][3]

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    prev = [0] * 4

    prev[0]= max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        temp = [0] * 4
        for last in range(0,4):
            temp[last] =0
            for task in range(0,3):
                if task!=last:
                    point = points[day][task] + prev[task]
                    temp[last] = max(temp[last], point)
        prev=temp

    return prev[3]