import sys

def solution() :
    N = int(sys.stdin.readline())
    count = [0] * 10001
    for _ in range(N):
        index = int(sys.stdin.readline())
        count[index] += 1

    for i in range(1, 10001) :
        if count[i] > 0 :
            print('%d\n'%i*count[i], end='')

solution()
