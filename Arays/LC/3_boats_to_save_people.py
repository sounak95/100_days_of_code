# https://leetcode.com/problems/boats-to-save-people/


def numRescueBoats( people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    people.sort()
    left=0
    right= len(people)-1

    boat_count=0

    while(left<=right):
        if left==right:
            boat_count+=1
            break

        if people[left]+people[right]<=limit:
            left+=1

        right-=1
        boat_count+=1
        # print(f"left: {left} right: {right} boat_count: {boat_count}")

    return boat_count

print(numRescueBoats([3,2,2,1],3))