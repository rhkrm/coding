def solution() :
    N = int(input())

    result = 666
    while N > 0 :
        while True :
            # print('result : ', result)
            # check 666 in mid
            temp = result
            flag = False
            while temp >= 666:
                # print('temp : ', temp)
                temp = int(temp/10)
                if temp % 1000 == 666:
                    N -= 1
                    flag = True
                    # print('1 N, result : ', N, result)
                    if N == 0:
                        print(result)
                        return
                    break

            # check 666 in end
            if flag == False and result % 1000 == 666 :
                N -= 1
                # print('2 N, result : ', N, result)
                if N == 0:
                    print(result)
                    return
                break

            result += 1
        result += 1

solution()
