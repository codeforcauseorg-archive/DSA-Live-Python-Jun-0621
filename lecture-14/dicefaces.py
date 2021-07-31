def dice(target, faces):

    if target == 0:
        return 1

    count = 0
    for face in range(1, faces+1):
        if face > target:
            break
        count += dice(target-face, faces)

    return count


def dicepaths(target, faces, solution=[]):

    if target == 0:
        print(solution)
        return

    for face in range(1, faces+1):
        if face > target:
            break
        solution.append(face)
        dicepaths(target-face, faces, solution)
        solution.pop()
    return


dicepaths(4, 3)



