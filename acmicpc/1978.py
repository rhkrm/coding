def solution() :
    case_num = int(input())

    result_count = 0

    case_list = list(map(int, input().split()))
    for i in range(case_num) :
        num = case_list[i] -1
        while num >= 2 :
            if case_list[i] % num == 0 :
                break
            num -= 1

        if num == 1 :
            result_count += 1


    print(result_count)

    return

solution()
