import math
def solution() :
    case_num = int(input())

    for _ in range(case_num) :
        n = int(input())
        prime = [True]*(n+1)
        prime[0] = prime[1] = False

        for i in range(2, int(math.sqrt(n))+1) :
            if prime[i] == True :
                for j in range(i+i, n+1, i) :
                    prime[j] = False

        result = []
        for i in range(int(n/2)+1) :
            if prime[i] == True and prime[n-i] == True:
                result.append([i, n-i])
        # print(result)
        print(result[-1][0], result[-1][1])

solution()
