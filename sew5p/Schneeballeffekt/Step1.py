import math


def copy_files(listOfPcsWithoutFile, PCsWithFile):

    while len(listOfPcsWithoutFile) > 0:
        for i in range(min(len(PCsWithFile),len(listOfPcsWithoutFile))):
            kopierZuPC = listOfPcsWithoutFile.pop()
            print(f"PC: {PCsWithFile[i]} zu PC:{kopierZuPC}")
            PCsWithFile.append(kopierZuPC)
        print("next Step...")


list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
list2 = [17]
copy_files(list1,list2)