def get_indices_of_item_weights(weights, length, limit):
    weightDict = { weights[i] : i for i in range(0, length) }
    print(weightDict)

    for i in range(length):
        currentWeight = weights[i]
        subNum = limit - currentWeight

        # print("Current weight", currentWeight)
        # print("Sub Num", subNum)
        # print("Current weight index", weightDict[currentWeight])

        if length <= 1:
            return None
        elif limit == (weights[0] + weights[1]):
            return (1, 0)
        elif subNum in weightDict:
            # print("Sub Num index", weightDict[subNum])
            return (max(weightDict[currentWeight], weightDict[subNum]), min(weightDict[currentWeight], weightDict[subNum]))

    return None

# weights = [ 4, 6, 10, 15, 16 ]
# length = 5
# limit = 21

# weights = [ 4, 4 ]
# length = 2
# limit = 8

# print(get_indices_of_item_weights(weights, length, limit))