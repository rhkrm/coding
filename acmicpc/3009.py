def solution() :
    x_index = []
    y_index = []

    for i in range(3) :
        input_x, input_y = map(int, input().split())
        if not input_x in x_index :
            x_index.append(input_x)
        else :
            x_index.remove(input_x)
        if not input_y in y_index :
            y_index.append(input_y)
        else :
            y_index.remove(input_y)

    print(x_index[0], y_index[0])

solution()
