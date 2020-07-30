def adjacentElementsProduct(inputArray):
    max = -1000 # set to smallest possible input
    for i in range(0, len(inputArray)-1):
        now = inputArray[i] * inputArray[i+1]
        if now > max:
           max = now
    return max
