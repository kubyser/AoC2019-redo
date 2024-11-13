START = 382345
END = 843167

PART2 = True

def nextNum(curNum):
    if len(curNum) == 6:
        hasDouble = False
        if not PART2:
            for p in range(0, len(curNum)-1):
                if curNum[p] == curNum[p+1]:
                    hasDouble = True
        else:
            rep = 0
            for p in range(0, len(curNum)-1):
                if curNum[p] == curNum[p+1]:
                    rep += 1
                else:
                    if rep == 1:
                        hasDouble = True
                    rep = 0
            if rep == 1:
                hasDouble = True
        if hasDouble and START <= int(curNum) <= END:
            print(curNum)
            return 1
        else:
            return 0
    res = 0
    for x in range(int(curNum[-1]), 10):
        xChar = str(x)
        res += nextNum(curNum + xChar)
    return res

numValid = 0
for i in range(3, 9):
    numValid += nextNum(str(i))
print("Valid codes: ", numValid)