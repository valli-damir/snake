# import random
#
# width = 10
# height = 10
# snake = [(0, 0)]
# direction = (1, 0)
# # food = (random.randint(0, width - 1), random.randint(0, height - 1))
#
#
# # class game:
#
#     def board():
#         for y in range(height):
#             for x in range(width):
#                 if (x, y) in snake:
#                     print('O', end=' ')
#                 elif (x, y) == food:
#                     print('X', end=' ')
#                 else:
#                     print('.', end=' ')
#             print()
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#         def __eq__(self, other):
#             return self.x == other.x and self.y == other.y
#
#         def __repr__(self):
#             global direction
#         x = input("Введите направление (w - вверх, s - вниз, a - влево, d - вправо): ").lower()
#         if x == 'w':
#             input("Введите на какое колличество клеток хотите сходить: ")
#             return f"direction({self.x}, {self.y - 1})"
#         elif x == 's':
#             input("Введите на какое колличество клеток хотите сходить: ")
#             return f"direction({self.x}, {self.y + 1})"
#         elif x == 'a':
#             input("Введите на какое колличество клеток хотите сходить: ")
#             return f"direction({self.x - 1}, {self.y})"
#         elif x == 'd':
#             input("Введите на какое колличество клеток хотите сходить: ")
#             return f"direction({self.x + 1}, {self.y})"
#
# game()
