import sys

def solution() :
    N = int(sys.stdin.readline())
    str_list = []
    for _ in range(N) :
        str_list.append(sys.stdin.readline()[:-1])

    # print(str_list)
    str_list = list(set(str_list))
    # print(str_list)
    str_list.sort(key=lambda x: (len(x), x))
    # print(str_list)
    for i in str_list :
        print(i)
solution()
