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

data = [trial() for _ in range(40000)]
ave = sum(data) / len(data)
dev_square = [(data[i] - ave) ** 2 for i in range(len(data))]
unbiased_var = sum(dev_square) / (len(data) - 1)
std_err = (unbiased_var / len(data)) ** (1/2)
print("期待値の推定値: " + str(ave))
print("推定誤差: " + str(std_err))
