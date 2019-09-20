import sys

def solution() :
    N = int(sys.stdin.readline())
    str_list = []
    for _ in range(N) :
        str_list.append(sys.stdin.readline().split())


    str_list.sort(key=lambda x: int(x[0]))
    # print(str_list)

    for i in str_list :
        print(i[0], end=' ')
        print(i[1])

solution()
