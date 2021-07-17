def dicegame(target):

    if target == 0:
        return 1

    if target < 0:
        return 0

    left = dicegame(target-1)
    right = dicegame(target-2)
    return left + right


dicegame(4)