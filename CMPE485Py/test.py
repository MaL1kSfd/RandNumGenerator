from prettytable import PrettyTable
import math

seed = 27
count = 1000
binCount = 0

randomNum = []

randoms = PrettyTable(["Bin No.", "Bin Lower Limit", "Bin Higher Limit", "Bin-Count"])

def RandomGen(x, count):
    nextRand = 0
    a = 101; c = 3; m = 10000 

    for i in range(count): 
        #Xi+1
        nextRand = (a*x+c) % m
        x = nextRand

        randomNum.append(nextRand/m)

        #print(nextRand)

file_path = "RN-file.txt"


def SaveRNs():
    try:
        with open(file_path, "w") as file:
            for rn in randomNum:
                file.write(str(rn) + " ")
        print(f"txt file '{file_path}' was created")
    except FileExistsError:
        print("That file already exists!")


def RetrieveRands():
    global binCount
    i = 1
    for rn in randomNum:
        if (rn < 0.1):
            binCount += 1
    print(binCount)        
    # for tr in range(10):
    #     lower = math.floor(rn * 10) / 10
    #     randoms.add_row([i, lower, lower + 0.0999, binCount])
    #     i += 1
        
    #print(randoms)    
        

RandomGen(seed, count)
SaveRNs()
RetrieveRands()


#do chi-square test


