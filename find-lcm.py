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
print(lcm(*range(2,14)))
