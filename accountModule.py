


class accnout():

    def __init__(self,
                 Cash=100000,
                 ):
        # initializing
        # cash
        self.cash = Cash
        self.total = Cash
        self.cost = 0
        self.chunk = 0
    def update(self, curPrice, curCost = 200):
        self.cost += curCost
        self.cash -= curCost
        # 总资产
        self.total = self.cash + self.chunk * curPrice

    def calIncome(self, curPrice):

        # 收益
        self.income = self.chunk * curPrice - self.cost
        # 收益率
        self.incomePercent = 0 if(self.cost == 0) else self.income / self.cost
        return self.incomePercent



