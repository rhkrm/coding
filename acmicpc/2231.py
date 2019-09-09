def solution() :
    N = int(input())
    result = 0
    for i in range(int(N/2), N) :
        #print("i : ", i)
        temp = i
        sum_temp = i
        while True :
            sum_temp += temp % 10
            if int(temp / 10) == 0 :
                break
            temp = int(temp / 10)

        if sum_temp == N :
            result = i
            break

    print(result)

solution()
