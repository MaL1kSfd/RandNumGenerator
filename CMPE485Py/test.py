seed = 27

randomNumBetweenZeroAndOne = [0.0] * 4 

def RandomGen(x):
    nextRand = 0
    a = 17; c = 43; m = 100

    i = 0
    while nextRand != 27:
        #Xi+1
        nextRand = (a*x+c) % m
        x = nextRand
        # for rand in range(len(randomNumBetweenZeroAndOne)):
        #     randomNumBetweenZeroAndOne[rand] = nextRand/m
        randomNumBetweenZeroAndOne[i] = nextRand/m
        i += 1

        print(nextRand)


RandomGen(seed)
print(randomNumBetweenZeroAndOne)

#do chi-square test


