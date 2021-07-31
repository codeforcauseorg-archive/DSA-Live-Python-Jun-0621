def subseq(unproc, index=0, proc=[]):

    if index == len(unproc):
        print(proc)
        return

    ch = unproc[index]

    proc.append(ch)
    subseq(unproc, index+1, proc)
    proc.pop()

    subseq(unproc, index + 1, proc)


subseq("abcdefghij")





