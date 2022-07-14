import numpy as np
import pandas as pd
from QueryDataModule import QueryData


class accnout():

    def __init__(self,
                 Cash=100000
                 ):
        # initializing
        # cash
        self.cash = Cash
        self.total = Cash
        self.maxCost = 0


    def Income(data, bucks=2000, buy=-0.05, sell=0.3, tax=0):
        print(bucks)
        times = 0
        cost = 0
        cash = 100000
        chunk = 0
        maxCost = 0
        # 日期，收益，收益率，空0买1卖2
        res = [[], [], [], []]

        for i in range(len(data[:, 0])):
            # 记录日期
            res[0].append(data[i, 0])
            # 计算收益情况
            cur = data[i, 1]
            income = chunk * cur - cost
            # 记录收益
            res[1].append(income)
            # 计算收益比例
            incomePercent = 0 if (cost == 0) else income / cost
            res[2].append(incomePercent)
            if incomePercent > sell:
                # sell
                cost -= bucks
                cash += bucks
                curChunk = (bucks - (tax * bucks)) / cur
                chunk -= curChunk
                times += 1
                res[3].append(2)
            elif incomePercent < buy or incomePercent == 0:
                # buy
                curChunk = (bucks - (tax * bucks)) / cur
                cost += bucks
                cash -= bucks
                if maxCost < cost:
                    maxCost = cost
                chunk += curChunk
                times += 1
                res[3].append(1)
            else:
                res[3].append(0)

        total = int(cash + chunk * cur)
        return res, total, maxCost, times

if __name__ == '__main__':
    # 对一个传入的data来说，中文名，ID，日期和对应的价格
    myquery = QueryData('jupyter notebook/fundinfo.csv')
    selectdata = myquery.QueryByName('博时上证超大盘')
    # print(selectdata)
    testdata = np.array( selectdata.values)
    # print(testdata)
    a = [0,2]
    id_name = testdata[:, a].astype(str)
    for i in range(len(id_name[:,0])):
        curID = id_name[i,0]
        while len(curID) < 6:
            curID = '0' + curID
        id_name[i,0] = curID

    cal = accnout()
    for code_name in id_name:
        code = code_name[0]
        name = code_name[1]
        #     try:
        pf = pd.read_csv('data/' + code + '.csv')
        outdata = pf.values
        data = outdata[:, 1:3]
        for bucks in range(100, 5000, 100):
            print(bucks)
            # res, total, maxCost, times = cal.Income(outdata, name, bucks=buck)
            buy = -0.05
            sell = 0.3
            tax = 0
            times = 0
            cost = 0
            cash = 100000
            chunk = 0
            maxCost = 0
            # 日期，收益，收益率，空0买1卖2
            res = [[], [], [], []]

            for i in range(len(data[:, 0])):
                # 记录日期
                res[0].append(data[i, 0])
                # 计算收益情况
                cur = data[i, 1]
                income = chunk * cur - cost
                # 记录收益
                res[1].append(income)
                # 计算收益比例
                incomePercent = 0 if (cost == 0) else income / cost
                res[2].append(incomePercent)
                if incomePercent > sell:
                    # sell
                    cost -= bucks
                    cash += bucks
                    curChunk = (bucks - (tax * bucks)) / cur
                    chunk -= curChunk
                    times += 1
                    res[3].append(2)
                elif incomePercent < buy or incomePercent == 0:
                    # buy
                    curChunk = (bucks - (tax * bucks)) / cur
                    cost += bucks
                    cash -= bucks
                    if maxCost < cost:
                        maxCost = cost
                    chunk += curChunk
                    times += 1
                    res[3].append(1)
                else:
                    res[3].append(0)

            total = int(cash + chunk * cur)
            print('total:%d'%total)
            print('MaxCost:%d'%maxCost)