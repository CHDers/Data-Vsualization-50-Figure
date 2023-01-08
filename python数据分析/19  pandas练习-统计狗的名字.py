# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 11:59
import pandas as pd

df = pd.read_csv('D:/python数据处理——数据/DataAnalysis-master/day04/dogNames2.csv')
# print(df.head())
# print(df.info())

# DataFrame中排序的方法
df = df.sort_values(by='Count_AnimalName',ascending=False)
# print(df.head(10))

# pandas取行或者列的注意事项
# 1.方括号写数字，表示取行，对行进行操作
# 2.方括号写字符串，表示取列索引，对列进行操作
print(df[:20])
print(df[:20]['Row_Labels'])
