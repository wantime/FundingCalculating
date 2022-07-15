import pandas as pd
import numpy as np

class QueryData():

    def __init__(self, dataPath='FundInfo.csv'):
        self.data = pd.read_csv(dataPath)

    def QueryByType(self, query):
        query_data = self.data.loc[self.data['type'].str.contains(query)]
        return query_data

    def QueryByName(self, query):
        query_data = self.data.loc[self.data['name'].str.contains(query)]
        return query_data

    def QueryById(self, query):
        query_data = self.data.loc[self.data['id'].str.contains(query)]
        return query_data

    def QueryByPY(self, query):
        query_data = self.data.loc[self.data['pinyin'].str.contains(query)]
        return query_data

    def QueryByFullPY(self, query):
        query_data = self.data.loc[self.data['Fullpinyin'].str.contains(query)]
        return query_data


def main():
    myquery = QueryData('jupyter notebook/fundinfo.csv')
    data = myquery.QueryByName('易方达')
    print(data)

if __name__ == '__main__':
    main()
