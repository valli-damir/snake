from time import sleep


def draw_field():
    for i in range(0, 12):
        for j in range(0, 12):
            if (i == 0 or i == 11) or (j == 0 or j == 11):
                print("*", end=" ")
            else:
                print(0, end=" ")
        print()
    print()


def draw_snake(x, y):
    for i in range(0, 12):
        for j in range(0, 12):
            if (i == 0 or i == 11) or (j == 0 or j == 11):
                print("*", end=" ")
            elif j == x and i == y:
                print("∆", end=" ")
            else:
                print(0, end=" ")
        print()
    print()
    return (x, y)


# def snake(x, y):
#     for i in range(0, 12):
#         for j in range(0, 12):
#             if (i <= 0):
#                 print(i == 11)
#             elif (j <= 0):
#                 print(j == 11)
#             elif (i >= 12):
#                 print(i == 1)
#             elif (j >= 0):
#                 print(j == 1)
#             else:
#                 print(0, end=" ")
#         print()
#     print()
#     return (x, y)


if __name__ == '__main__':
    x = 1
    y = 1
    draw_field()
    draw_snake(x, y)
    # snake(x, y)


    def move(direction):
        match direction:
            case "w":
                return draw_snake(x, y - 1)
            case "s":
                return draw_snake(x, y + 1)
            case "a":
                return draw_snake(x - 1, y)
            case "d":
                return draw_snake(x + 1, y)
            case _:
                print("Не правильное напрвление! ")


    for i in range(0, 10):
        x, y = move(input())
