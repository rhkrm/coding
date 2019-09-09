def solution() :
    while True :
        x, y, z = map(int, input().split())
        if x == 0 :
            break

        max_line = max(x, y, z)

        if x == max_line and x*x == y*y + z*z :
            print("right")
        elif y == max_line and y*y == x*x + z*z :
            print("right")
        elif z == max_line and z * z == x * x + y * y :
            print("right")
        else :
            print("wrong")


solution()
