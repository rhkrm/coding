def solution() :
    case_num = int(input())

    case_list = []
    for _ in range(case_num) :
        case_list.append(list(map(int, input().split(' '))))

    result = [1]*case_num
    for i in range(case_num) :
        for j in range(case_num) :
            if i == j :
                continue
            if case_list[i][0] > case_list[j][0] and case_list[i][1] > case_list[j][1] :
                result[j] += 1
    for k in result :
        print(k, end=' ')
solution()
