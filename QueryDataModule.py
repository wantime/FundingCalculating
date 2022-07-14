import pandas as pd
import numpy as np

class QueryData():

    def __init__(self, dataPath='FundInfo.csv', converters={'id':str}):
        self.data = pd.read_csv(dataPath, converters={'id': str})

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

    # def Query(self, col, query):
    #     match col:
    #         case 1:
    #             return self.QueryById(query)
    #         case 2:
    #             return self.QueryByPY(query)
    #         case 3:
    #             return self.QueryByName(query)
    #         case 4:
    #             return self.QueryByType(query)
    #         case 5:
    #             return self.QueryByFullPY(query)
    #         case other:
    #             print('Wrong Input type or value of parameter col, only 1-5.')

def main():
    myquery = QueryData('data/fundinfo.csv')
    data = myquery.QueryByName('易方达')
    print(data)

if __name__ == '__main__':
    main()
