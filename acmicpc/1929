import math
def solution() :
    start_num, end_num = map(int, input().split())

    result_list = [True]*(end_num+1)
    result_list[0] = False
    result_list[1] = False

    for i in range(2, int(math.sqrt(end_num))+1) :
        if result_list[i] == True :
            for j in range(i+i, end_num+1, i) :
                result_list[j] = False

    for i in range(start_num, end_num+1) :
        if result_list[i] == True :
            print(i)

    return

solution()
