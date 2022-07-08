import pandas as pd
import numpy as np
import accountModule
import matplotlib.pyplot as plt


def exchange(curPrice, curMoney=2000, tax=0):
    curChunk = (curMoney - (tax * curMoney)) / curPrice
    return curChunk


if __name__ == "__main__":
    # 读取文本中的id号
    # f = open('id.txt', encoding='utf8')
    # ids = f.readlines()
    # time = 1
    # for id in ids:
    #     print(id)
    #     print(time)
    #     time += 1
    # 模拟智能定投，计算最终获利情况
    # ids = ['001631', '012348', '050026']
    # for id in ids:
    #     df = pd.read_csv(id+'.csv')
    #     data = df.values
    #     value = data[:,2]
    #
    #     times = 0
    #     cost = 0
    #     cash = 100000
    #     chunk = 0
    #     exchanges = 0
    #     bucks = 5000
    #     list  = []
    #     for cur in value:
    #         # 计算收益情况
    #         income = chunk * cur - cost
    #         # 计算收益比例
    #         incomePercent = 0 if (cost == 0) else income / cost
    #
    #
    #         if incomePercent > 0.3:
    #             # sell
    #             cost -= bucks
    #             cash += bucks
    #             curChunk = exchange(cur, curMoney=bucks)
    #             chunk -= curChunk
    #             times += 1
    #         elif incomePercent < -0.05 or incomePercent == 0:
    #             # buy
    #             curChunk = exchange(cur, curMoney=bucks)
    #             cost += bucks
    #             cash -= bucks
    #             chunk += curChunk
    #             times += 1
    #
    #         list.append(income)
    #
    #     cur = value[len(value) - 1]
    #     total = cash + chunk * cur
    #     print(times)
    #     print(total)
    #     savedata = pd.Series(list)
    #     savedata.to_csv(id+'_income.csv', encoding='utf8')
    #     plt.figure()
    #     plt.plot(list)
    #     plt.show()
    
    # 获取所有的基金编号

    pass


