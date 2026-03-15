seed = 27
count = 10000

randomNumBetweenZeroAndOne = []

def RandomGen(x, count):
    nextRand = 0
    a = 101; c = 3; m = 10000 #make c and m coprime

    for i in range(count): 
        #Xi+1
        nextRand = (a*x+c) % m
        x = nextRand

        #randomNumBetweenZeroAndOne[i] = nextRand/m
        randomNumBetweenZeroAndOne.append(nextRand/m)

        print(nextRand)


RandomGen(seed, count)
print(randomNumBetweenZeroAndOne)

#do chi-square test


