import math
def solution() :
    case_list = []
    while(True) :
        n = int(input())
        if n == 0 :
            break
        case_list.append(n)

    for i in case_list :

        prime = [True]*(2*i +1)

        prime[0] = False
        prime[1] = False

        n = int(math.sqrt(2*i))

        for j in range(2, n+1) :
            if prime[j] == True :
                for k in range(j+j, 2*i+1, j) :
                    prime[k] = False

        count = 0
        for j in range(i+1, 2*i+1) :
            if prime[j] == True :
                count += 1

        print(count)

solution()
