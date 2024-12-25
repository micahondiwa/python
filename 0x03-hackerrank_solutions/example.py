# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    count = 0
    while "B" in S and "A" in S and "N" in S:
        bindex = S.find("B")
        if bindex == -1:
            break
        aindex = S.find("A")
        if aindex == -1:
            break
        nindex = S.find("N")
        if nindex == -1:
            break
        n2index = S.find("N")
        if n2index == -1:
            break
        count += 1
        S = S[:bindex] + S[bindex + aindex + n2index + 3:]
    return count
