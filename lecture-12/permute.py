def permut(unproc, proc):

    if len(unproc) == 0:
        print(proc)
        return

    for index in range(len(unproc)):
        ch = unproc[index]
        permut(unproc[:index]+unproc[index+1:], proc+ch)


permut("abc", "")