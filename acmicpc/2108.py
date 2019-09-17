import sys
from collections import Counter

def solution() :
    N = int(sys.stdin.readline())
    num_list = []
    for _ in range(N) :
        num_list.append(int(sys.stdin.readline()))

    num_list.sort()
    # 1
    result = sum(num_list)/len(num_list)
    print(round(result))

    # 2
    print(num_list[int(len(num_list)/2)])

    # 3
    count_list = Counter(num_list)
    count_list = count_list.most_common()
    #print(count_list)
    max_num = count_list[0][1]
    result = []
    for i in count_list :
        if max_num == i[1] :
            result.append(i[0])
    #print(result)
    result.sort()
    if len(result) > 1 :
        print(result[1])
    else :
        print(result[0])

    # 4
    print(num_list[-1]-num_list[0])

solution()
