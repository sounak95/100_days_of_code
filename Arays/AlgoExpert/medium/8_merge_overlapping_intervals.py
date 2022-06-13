
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals=sorted(intervals,key=lambda x:x[0])
    merged_intervals=[]
    currentInterval= sortedIntervals[0]
    merged_intervals.append(currentInterval)

    for nextInterval in sortedIntervals[1:]:
        _, currentIntervalEnd=currentInterval
        nextIntervalStart, nextIntervalEnd =nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            merged_intervals.append(currentInterval)

    return merged_intervals

intervals=[[1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]]

intervals=[[1, 10],
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50],
    [50, 60],
    [60, 70],
    [70, 80],
    [80, 90],
    [90, 100]]
print(mergeOverlappingIntervals(intervals))