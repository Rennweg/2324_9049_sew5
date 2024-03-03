import heapq
def copy_files(listOfPcsWithoutFile, PCsWithFile):

    while len(listOfPcsWithoutFile) > 0:
        for i in range(len(PCsWithFile)):
            if not copy(PCsWithFile, i, listOfPcsWithoutFile):
                return
            if PCsWithFile[i][0] == 1:
                if not copy(PCsWithFile, i, listOfPcsWithoutFile):
                    return
        print("next Step...")


def copy(PCsWithFile, i, listOfPcsWithoutFile):
    if len(listOfPcsWithoutFile) == 0:
        return False
    kopierZuPC = heapq.heappop(listOfPcsWithoutFile)
    print(f"PC: {PCsWithFile[i]} zu PC:{kopierZuPC}")
    PCsWithFile.append(kopierZuPC)

    return True


list1 = [(1,2),(2,2),(3,2),(4,1),(5,2),(6,2),(7,2),(8,2),(9,2),(10,1),(11,1),(12,1),(13,1),(14,2),(15,1),(16,1)]
a = []
for t,u in list1:
    heapq.heappush(a, (u,t))
list2 = [(1,17)]
copy_files(a,list2)