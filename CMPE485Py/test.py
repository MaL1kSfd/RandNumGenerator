from prettytable import PrettyTable

seed = 27
count = 1000

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

def ListToTable():
    for rn in randomNum:
        match randomNum[rn]:
            case 1:
                print("Pip")

    print("Stuff")

def SaveRNs():
    try:
        with open(file_path, "w") as file:
            for rn in randomNum:
                file.write(str(rn) + " ")
        print(f"txt file '{file_path}' was created")
    except FileExistsError:
        print("That file already exists!")


RandomGen(seed, count)
print(randomNum)
SaveRNs()

#do chi-square test


