def subseq(orig, proc, index):

    if index == len(orig):
        print(proc)
        return

    ch = orig[index]

    subseq(orig, proc + ch, index+1)
    subseq(orig, proc, index+1)


subseq("abc", "", 0)

