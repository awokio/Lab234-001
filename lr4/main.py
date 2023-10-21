import random
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



def method1(n: int) -> list:
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data



def method2(k: int):
    res = random.sample(range(1, 6), k)
    return res




def method3(j: int):
    res = [random.randrange(1, 7, 1) for i in range(j)]
    return res



def method4(n):
    lis = []
    for _ in range(n):
        lis.append(random.randint(1, 6))
    return lis



def method5(m):
    a = list(np.random.randint(low = 1,high=7,size=m))
    return(a)




def method6(p):
    b = np.random.random_sample(size = p)
    return b





# def kubik(n: int) -> list:
#     data = []
#     while len(data) < n:
#         data.append(random.randint(1, 6))
#     return data


def count_rate(kubik: list):
    kub_rate = {}
    for i in kubik:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kubik.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate


def sort_rate(counted_rate: dict):
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def create_dataframe(sorted_date: dict):
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))


    po = []
    for i in range(1, 7):
        o = sorted_date.get(i)
        po.append(o)

    xdata = [1, 2, 3, 4, 5, 6]
    ydata = po
    # plt.bar(xdata, ydata, color="green")
    # plt.bar(xdata, ydata, color="red")
    # plt.bar(xdata, ydata, color="lightblue")
    plt.bar(xdata, ydata, color="yellow")
    plt.show()
    return df



dff = create_dataframe(sort_rate(count_rate(method5(1000000))))
print(dff)


