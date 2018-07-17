import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import time

# B.1.フォルダ (regression) 内のデータファイル (data.csv) を読み込め.
data_csv = pd.read_csv('../data/data.csv')
data_import = np.array(data_csv)

# B.2.読み込んだデータを可視化せよ.
x = data_import[:,0]
y = data_import[:,1]
plt.scatter(x,y, color='blue', s=5,label='data set')
x_max = np.max(data_import[:,0])
x_min = np.min(data_import[:,0])
y_max = np.max(data_import[:,1])
y_min = np.min(data_import[:,1])
plt.xlim(x_min+x_min/10,x_max+x_max/10)
plt.ylim(y_min+y_min/10,y_max+y_max/10)
plt.grid(color='gray')
plt.legend()
plt.show()

# B.3.読み込んだデータを訓練データとテストデータに分割せよ.
train_number = 800
data_import = shuffle(data_import)
data_train ,data_test = np.split(data_import,[train_number])

# B.4.N (1 ≤ N ≤ 5) 次関数を用いて回帰を行え.ただし,回帰には勾配降下法を用いよ.
# B.5.回帰の結果を元に,データと回帰線を可視化せよ.

# ウェイトの定義
w = np.array([np.random.random(i+2) for i in range(5)])

def deru(x_input, sample, w):
    y_target = sample[:,1]
    y_out = np.dot(w, x_input.T)
    errors = y_target - y_out
    return errors

def rmse(x_input, sample, w):
    errors = deru(x_input, sample, w)
    error2 = np.sum(errors**2)
    return np.sqrt(error2/sample.shape[0])

#1次
time_sokutei = np.zeros(5)
start1 = time.time()
x1_sample = data_train
x_input = np.array([x1_sample[:,0]]).T
x = [x_input**i for i in range(6)] 
x2 = np.empty((x_input.shape[0],6)) #次数+1
for i in range(6):
    x2[:,i] = x[i][:,0]
#print(x2.shape)
#print(x2)
for i in range (2000):
    for j in range (5):
        start = time.time()
        errors = deru(x2[0::,0:j+2], x1_sample, w[j])
        w[j] += 0.00001*np.dot(errors.T, x2[0::,0:j+2])
        time_sokutei[j] += time.time()-start



    '''
    start = time.time()
    errors = deru(x2[0::,0:2], x1_sample, w[0])
    w[0] += 0.001*np.dot(errors.T, x2[0::,0:2])
    time_sokutei[0] += time.time()-start

    start = time.time()
    errors = deru(x2[0::,0:3], x1_sample, w[1])
    w[1] += 0.0001*np.dot(errors.T, x2[0::,0:3])
    time_sokutei[1] += time.time()-start

    start = time.time()
    errors = deru(x2[0::,0:4], x1_sample, w[2])
    w[2] += 0.0001*np.dot(errors.T, x2[0::,0:4])
    time_sokutei[2] += time.time()-start

    start = time.time()
    errors = deru(x2[0::,0:5], x1_sample, w[3])
    w[3] += 0.000001*np.dot(errors.T, x2[0::,0:5])
    time_sokutei[3] += time.time()-start

    start = time.time()
    errors = deru(x2[0::,0:6], x1_sample, w[4])
    w[4] += 0.000001*np.dot(errors.T, x2[0::,0:6])
    time_sokutei[4] += time.time()-start
    '''

plt.title('result')
x_plot = np.empty((6,40))
y_plot = np.empty((5,40))
x1_plot = np.arange(x_min, x_max, 0.1)
x2_plot = [x1_plot**i for i in range(6)]
for i in range(6): # 次数+1
    x_plot[i,:] = x2_plot[i]
#print(x_plot.shape)
for i in range(5):
    y_plot[i] = np.dot(w[i], x_plot[0:i+2,0::])

plt.plot(x1_plot,y_plot[0],label='1-order prediction')
plt.plot(x1_plot,y_plot[1],label='2-order prediction')
plt.plot(x1_plot,y_plot[2],label='3-order prediction')
plt.plot(x1_plot,y_plot[3],label='4-order prediction')
plt.plot(x1_plot,y_plot[4],label='5-order prediction')
x = data_import[:,0]
y = data_import[:,1]
plt.xlim(x_min+x_min/10,x_max+x_max/10)
plt.ylim(y_min+y_min/10,y_max+y_max/10)
plt.scatter(x,y, color='blue', s=5,label='data set')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='gray')
plt.legend()
plt.show()

# B.6.N (1 ≤ N ≤ 5) 次近似の結果からテスト誤差 (RMSE) を小数第3位まで求めよ.
x_sample = np.array(data_test[:,0]).T
#print(x_sample)
x_test = [x_sample**i for i in range(6)]
x2_test = np.empty((data_test.shape[0],6)) #次数+1
for i in range(6):
    x2_test[:,i] = x_test[i]
print(x_test)
print(x2_test)
#1次
rmse1 = rmse(x2_test[0::,0:2], data_test, w[0])
print('N=1 {:.3f} {:.3f}'.format(rmse1,time_sokutei[0]))

#2次
rmse2 = rmse(x2_test[0::,0:3], data_test, w[1])
print('N=2 {:.3f} {:.3f}'.format(rmse2,time_sokutei[1]))

#3次
rmse3 = rmse(x2_test[0::,0:4], data_test, w[2])
print('N=3 {:.3f} {:.3f}'.format(rmse3,time_sokutei[2]))

#4次
rmse4 = rmse(x2_test[0::,0:5], data_test, w[3])
print('N=4 {:.3f} {:.3f}'.format(rmse4,time_sokutei[3]))

#5次
rmse5 = rmse(x2_test[0::,0:6], data_test, w[4])
print('N=5 {:.3f} {:.3f}'.format(rmse5,time_sokutei[4]))
    
