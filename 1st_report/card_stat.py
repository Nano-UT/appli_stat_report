from random import shuffle

def trial():
    lis = [i//4 for i in range(52)]
    shuffle(lis)
    tmp = 1
    while(True):
        if len(lis) < 5:
            return(20)
        if len(lis[:5]) == len(set(lis[:5])):
            tmp += 1
            lis = lis[5:]
        else:
            return(tmp)
