

# https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1



def isRotated(str1, str2):
    anti_clock = str1[2:] + str1[0:2]
    clock_rot = str1[len(str1)-2:] + str1[0:len(str1)-2]

    # print(anti_clock)
    # print(clock_rot)
    return str2==anti_clock or str2== clock_rot

print(isRotated("amazon", "azonam"))
print(isRotated("amazon", "onamaz"))
