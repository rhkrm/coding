import sys
def solution() :
    N = int(sys.stdin.readline())
    list_num = []
    for _ in range(N):
        list_num.append(int(sys.stdin.readline()))

    list_num.sort()
    # result = [-1]*N
    # merge_sort(result, list_num, 0, N-1)

    for i in list_num :
        print(i)
solution()
