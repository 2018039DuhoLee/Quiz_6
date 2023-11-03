def draw_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

tree_height = int(input("높이를 입력하시오: "))

draw_christmas_tree(tree_height)









