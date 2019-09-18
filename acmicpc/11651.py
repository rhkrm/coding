import sys

from operator import itemgetter
def solution() :
    N = int(sys.stdin.readline())
    num_list = []
    for _ in range(N) :
        num_list.append(list(map(int, sys.stdin.readline().split())))

    # print(num_list)
    num_list = sorted(num_list, key=itemgetter(0))
    num_list = sorted(num_list, key=itemgetter(1))
    # print(num_list)
    for i in num_list :
        print(i[0], end=' ')
        print(i[1])

solution()
