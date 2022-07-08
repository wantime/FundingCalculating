from typing import List,Any,Union
import requests
import execjs
import pandas as pd

url = 'http://fund.eastmoney.com/js/fundcode_search.js'
content = requests.get(url)
jsContent = execjs.compile(content.text)
rawData = jsContent.eval('r')
allInfo: list[Union[list[str], Any]] = [["基金代码", "基金简拼", "基金名称", "基金类型", "基金全拼"]]
for code in rawData:
    allInfo.append(code)

save = pd.Series(allInfo)
save.to_csv('fundingID.csv', encoding='utf8')
for i in range(len(allInfo)):
    for j in range(len(allInfo[i])):
        print(allInfo[i][j], end='\t')
    print()