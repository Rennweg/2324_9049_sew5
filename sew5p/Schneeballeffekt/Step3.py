import heapq
from collections import defaultdict

def copy_files(pcWithout, pcWith):
    time = 0
    minTime = True
    dic = defaultdict(int)
    while True:
        if minTime == 0 and len(pcWithout) == 0:
            return
        print(f"Time: {time}")
        for i in range(min(len(pcWith), len(pcWithout))):
            if dic[pcWith[i][1]]==0:
                if not copy(pcWith, i, pcWithout, dic):
                    break

            if time % pcWith[i][1] == 0:
                if not copy(pcWith, i, pcWithout):
                    break
        time += 1
        for v, id in pcWith:
            if time % v > 0:
                allDone = False
                break
            allDone = True

def copy(pcWith, i, pcWithout, dic):
    if len(pcWithout) == 0:
        return False
    kopierZuPC = heapq.heappop(pcWithout)
    print(f"PC: {pcWith[i]} zu PC:{kopierZuPC}")
    dic[kopierZuPC] = pcWith[i][0]
    dic[pcWith[i][1]] = pcWith[i][0]

    pcWith.append(kopierZuPC)
    return True


list1 = [(1,50),(2,25),(3,75),(4,50),(5,50),(6,42),(7,48),(8,53),(9,29),(10,29),(11,50),(12,50),(13,79),(14,69),(15,80),(16,99)]
a = []
for t,u in list1:
    heapq.heappush(a, (u,t))
list2 = [(13,17)]
copy_files(a,list2)