import urllib.request
import numpy as np
import random
import matplotlib.pyplot as plt
import japanize_matplotlib

url = 'https://raw.githubusercontent.com/maskot1977/Statistics2017/master/home.txt'
urllib.request.urlretrieve(url, 'home.txt')
data = []
for line in open("home.txt"):
  c = line.split()
  c = c[:4]+[c[7]]
  data.append(c)
label = data[0]
print(label) #データのラベルを確認する
data = data[1:] #データからラベルを取り除く
Y = np.array([[int(i[0])] for i in data])
Xs = np.array([list(map(float, i[1:]))+[1] for i in data]) #最後の1は定数項

def multiple_regression(Y, Xs):
    return(np.dot(np.dot(np.linalg.inv(np.dot(Xs.T, Xs)), Xs.T), Y))

b = multiple_regression(Y, Xs)
print("回帰係数: ", *label[1:], " 定数項")
print(*b.T)
#回帰式を文章にする
regr_eq = label[0] + "="
for i in range(len(label[1:])):
    regr_eq = regr_eq + label[1:][i] + "*(" + str(int(b[i][0])) + ")+"
regr_eq = regr_eq + "(" + str(int(b[-1][0])) + ")"
print("回帰式: " + regr_eq)

#決定係数
Y_predict = np.dot(Xs, b)
ave_Y = sum(Y) / len(Y)
S_R = sum((Y_predict - ave_Y) ** 2)
S_T = sum((Y - ave_Y) ** 2)
print("決定係数: " + str(S_R / S_T))

#ブートストラップ法による回帰係数の標準誤差の推定
bs = [] #試行ごとの回帰係数
std_err_bs = [] #回帰係数ごとの標準誤差

for _ in range(100):
    boot_data = random.choices(data, k = len(data))
    boot_Y = np.array([[int(i[0])] for i in boot_data])
    boot_Xs = np.array([list(map(float, i[1:]))+[1] for i in boot_data])
    bs.append(multiple_regression(boot_Y, boot_Xs).T)

for k in range(len(bs[0][0])):
    b_k = [m[0][k] for m in bs]
    ave = sum(b_k) / len(b_k)
    dev_square = [(b_k[i] - ave) ** 2 for i in range(len(b_k))]
    unbiased_var = sum(dev_square) / (len(b_k) - 1)
    std_err_bs.append(unbiased_var ** (1/2))

print("回帰係数の標準誤差: ", *label[1:], " 定数項")
print(std_err_bs)
nx = np.linspace(5,20, 100)
plt.scatter(Y / 10000, Y_predict / 10000)
plt.plot(nx, nx, color="orange" , linestyle = "dashed")
plt.title("家賃とその予測値の散布図", fontsize=14)
plt.xlabel("家賃(万円)", fontsize=14)
plt.ylabel("家賃の予測値(万円)", fontsize=14)
plt.tick_params(labelsize=12)
plt.xlim([5,20])
plt.ylim([5,20])
plt.tight_layout()
plt.show()
