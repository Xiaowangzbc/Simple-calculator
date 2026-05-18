import pandas as pd
s = pd.Series([1,2,3],index=['a','b','c'])
df = pd.DataFrame({
    '姓名':['张三','李四','王五'],
    '年林':[25,30,50],
    '城市':['北京','上海','深圳']

})
print(s)
print(df)
姓名列 = df['姓名']
print(f'姓名列是\n{姓名列}')
print(df.info)