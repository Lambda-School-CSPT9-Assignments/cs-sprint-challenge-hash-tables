def has_negatives(a):
    posNum = []
    negNum = []

    result = []

    for i in range(len(a)):
        if a[i] < 0:
            negNum.append(abs(a[i]))
        else:
            posNum.append(a[i])

    negDict = {negNum[i] : i for i in range(0, len(negNum))}

    for i in range(len(posNum)):
        if posNum[i] in negDict:
            result.append(posNum[i])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
