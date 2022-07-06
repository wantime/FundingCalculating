import pandas as pd
import numpy as np
import accountModule


def exchange(curPrice, curMoney=2000, tax=0):
    curChunk = (curMoney - (tax * curMoney)) / curPrice
    return curChunk


if __name__ == "__main__":
    df = pd.read_csv('012348.csv')
    # dataValue = data.values
    data = df.values
    value = data[:,2]

    times = 0
    cost = 0
    cash = 100000
    chunk = 0
    exchanges = 0
    for cur in value:
        # 计算收益情况
        income = chunk * cur - cost
        # 计算收益比例
        incomePercent = 0 if (cost == 0) else income / cost


        if incomePercent > 0.4:
            # sell
            cost -= 2000
            cash += 2000
            curChunk = exchange(cur)
            chunk -= curChunk
            exchanges += 1
        elif incomePercent < -0.05 or incomePercent == 0:
            # buy
            curChunk = exchange(cur)
            cost += 2000
            cash -= 2000
            chunk += curChunk
            exchanges += 1
        print('交易次数:' + str(exchanges) + '收益是:' + str(income))

    cur = value[len(value) - 1]
    total = cash + chunk * cur
    print(total)
    # myAccount = accountModule()
    # flag = True
    # for i in value:
    #     if flag:
    #         buyChunk = buy(curPrice = i)
    #         myAccount.update(curPrice = i)
    #         flag = False

