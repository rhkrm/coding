def solution() :
    start_num = int(input())
    end_num = int(input())

    result_list = []

    for i in range(start_num, end_num+1) :
        if i == 2 :
            result_list.append(i)
            continue

        num = i-1
        while num >= 2 :
            if i%num == 0 or i%2 ==0:
                break
            num -= 1

        if num == 1 :
            result_list.append(i)

    if result_list :
        print(sum(result_list))
        print(result_list[0])
    else :
        print(-1)


    return

solution()
