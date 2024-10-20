import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)


labels = ['a','b','c']
my_List = [10, 20, 30]
arr = np.array([10,20,30])
d = {'a': 10,
     'b': 20,
     'c': 30
     }

# print(pd.Series(data=my_List))
# print(pd.Series(my_List,labels))
# print(pd.Series(data=arr))
# print(pd.Series(arr, labels))
# print(pd.Series(d))

# print(pd.Series(data=labels))
# print(pd.Series([sum,print,len]))


ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']) 
# print(ser1)

ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])  
# print(ser2)

# print(ser1['USA'])

# print(ser1 + ser2)




df = pd.DataFrame(randn(5,4) , index='A B C D E'.split() , columns='W X Y Z'.split())
# print(df)

# print(df['W'])

# print(df[['W','Z']])

# print(df.W)  NOT RECOMMENDED!

# print(type(df['W']))

# df['new'] = df['W'] +  df['Y']
# print(df)

# print(df.drop('new' , axis=1))
# print(df)
# df.drop('new',axis=1,inplace=True)
# print(df)

# print(df.drop('E',axis=0))




# print(df.loc['A'])
# print(df.iloc[2])
# print(df.loc['B','Y'])
# print(df.loc[['A','B'] , ['W','Y']])




# print(df)

# print(df>0)

# print(df[df>0])

# print(df[df['W']>0])
# print(df[df['W']>0]['Y'])

# print(df[df['W']>0][['Y','X']])
# print(df[(df['W']>0) & (df['Y'] > 1)])


print(df)


print(df.reset_index())