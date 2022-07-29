import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../Data/export_data_new.csv')
power655 = df["Power655"]
seq = [0]*56
for i in power655:
    for j in i.split("-"):
        if j != '':
            index = int(j)
            seq[index]=seq[index]+1
def plot_data(data):
    bin = np.arange(0,120,1)
    plt.hist(data, bins=bin)
    plt.show()
def bar(data):
    lable = [0]*56
    for i in range(0,56):
        lable[i] = i
    plt.bar(lable,data)
    plt.grid(True)
    plt.show()
bar(seq)