def solution() :
    N, M = map(int, input().split())
    card = list(map(int, input().split()))

    Max = 0
    for i in range(N-2) :
        for j in range(i+1,N-1) :
            for k in range (j+1, N) :
                if card[i]+card[j]+card[k] <= M :
                    Max = max(Max, card[i]+card[j]+card[k])
    print(Max)


solution()
