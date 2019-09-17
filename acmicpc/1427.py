import sys

def solution() :
    N = int(sys.stdin.readline())
    num_list = []
    while N >= 10 :
        num_list.append(int(N%10))
        N = int(N/10)
    num_list.append(N)

    num_list.sort(reverse=True)
    # print(num_list)
    for i in num_list :
        print(i, end='')

solution()
