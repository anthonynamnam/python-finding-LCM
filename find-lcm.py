import math
def lcm(*avgs):
    ans = 1
    num_list = list(avgs)
    for i in range(len(num_list),0,-1):
        for x in range(2,max(num_list)+1):
            allcommon = [y%x == 0 for y in num_list]
            if allcommon.count(True) == i:
                ans = ans * x
                num_list = [z//x if z%x == 0 else z for z in num_list]
            if max(num_list) <= x:
                break;
    for j in num_list:
        ans = ans * j
    return ans
# Find LCM of 2,3,4,5,6
print(lcm(*range(2,7))) # LCM = 60

# Find LCM of 3,5,7,29
print(lcm(3,5,7,29)) # LCM = 3045

# Find LCM of 20,30,120,280
print(lcm(20,30,120,280)) # LCM = 840

