from prettytable import PrettyTable
import math

seed = 27
count = 1000
bin1Count = 0
bin2Count = 0

randomNum = []
bins = [] * 10

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
    for rn in randomNum:
        index = math.floor(rn * 10) 
        if(index != 1):
            bins[index] += 1
        else:
            bins[index] += 1
    print(bins)       
    # for tr in range(10):
    #     lower = math.floor(rn * 10) / 10
    #     randoms.add_row([i, lower, lower + 0.0999, binCount])
    #     i += 1
        
    #print(randoms)    
        

# RandomGen(seed, count)
# SaveRNs()
# RetrieveRands()

# non = 10
# bon = min(math.floor(non * 10)) 
# print(bon)


#do chi-square test


