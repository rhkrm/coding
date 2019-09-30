import sys

def solution() :

    T = int(sys.stdin.readline())

    for _ in range(T) :
        n = int(sys.stdin.readline())
        fibo = [(1,0), (0,1)]

        if n == 0  or n == 1:
            print(fibo[n][0], fibo[n][1])
            continue

        for i in range(2, n+1) :
            fibo.append((fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]))

        print(fibo[-1][0], fibo[-1][1])

solution()
