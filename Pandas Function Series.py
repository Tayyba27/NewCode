 # Pandas  Function Series
import numpy as np
import pandas as pd

labels = [ 'a' , 'b' ,'c']

numpydata = np.array([10, 20, 30])

dic= {'a' :10 , 'b':20 ,'c': 30}

pd.Series(labels)

pd.Series(numpydata)

pd.Series(dic)
pd.Series(numpydata , labels)

# # Data Frame
import pandas as pd
import numpy as np
from numpy.random import randn


np.random.seed(101)

df = pd.DataFrame(randn(5,4) , ['A','B','C' ,'D' ,'E'] , ['w' ,'x', 'y' ,'z'])
print(df)

df['w']
type(df['w'])

type(df)
df[['w' ,'z']]

df['new'] = df['w'] + df['x']
print(df['new'])

print(df)
df.drop('new' ,axis = 1)


# inplace = True   means to drop the "new " permanently
df.drop('y' ,axis = 1 , inplace = True)

print(df)

# for select row
df.loc['A']

# FOR POSITION SELECTION
df.iloc[2]

df.loc['C' , 'new']

df.loc[['A' ,'B'] , [ 'w' ,'new']]
df


df>0
df[df>0]
df['w'] >0
df[df['w'] >0]
booldf = df['w'] >0
booldf
result = df[booldf]
result


mycols = ['x' , 'z']
result[mycols]
# # missing values

d = { 'A' : [1,2,np.nan] , 'B' : [5 , np.nan , np.nan] , 'C' : [1,2,3]}

df = pd.DataFrame(d)
df
# dropna command is temporary delete
df.dropna()

# delete the row
df.dropna( axis = 1)

# 2 se kam NaN wali row retaine rahy
df.dropna(thresh = 2)
df
df['A'].fillna(value = df['A'].mean())

#  maranging
df1 = pd.DataFrame({'A' : ['A0' , 'A1' , 'A2' , 'A3'] ,
                    'B ' : ['B0' , 'B1' , 'B2' , 'B3'] ,
                    'C' : ['C0' , 'C1' , 'C2' , 'C3'] ,
                    'D' : ['D0' , 'D1' , 'D2' , 'D3']},
                    index=[0,1,2,3])

# %%
df2 = pd.DataFrame({'A' : ['A4' , 'A5' , 'A6' , 'A7'] ,
                    'B ' : ['B4' , 'B5' , 'B6' , 'B7'] ,
                    'C' : ['C4' , 'C5' , 'C6' , 'C7'] ,
                    'D' : ['D4' , 'D5' , 'D6' , 'D7']},
                    index=[4,5,6,7])


df3 = pd.DataFrame({'A' : ['A8' , 'A9' , 'A10' , 'A11'] ,
                    'B ' : ['B8' , 'B9' , 'B10' , 'B11'] ,
                    'C' : ['C8' , 'C9' , 'C10' , 'C11'] ,
                    'D' : ['D8' , 'D9' , 'D10' , 'D11']},
                    index=[8,9,10,11])


left = pd.DataFrame({'key' : ['K0' , 'K1' , 'K2' , 'K3'] ,
                     'A':   ['A0' ,'A1' ,'A2' , 'A3'],
                    'B ' : ['B0' , 'B1' , 'B2' , 'B3']})

                    
right  = pd.DataFrame({'key' : ['K0' , 'K1' , 'K2' , 'K3'] ,  
                    'C' : ['C8' , 'C9' , 'C10' , 'C11'] ,
                    'D' : ['D8' , 'D9' , 'D10' , 'D11']})
                                    


df1

df2

df3

pd.concat([df1 , df2 , df3])

# along column
pd.concat([df1 , df2 , df3] , axis = 1)

left
right
pd.merge(left,right , how= 'inner' , on = 'key')
# # Operation read and write DataFrames
import pandas as pd
df = pd.DataFrame({'col1' : [1,2,3,4] , 'col2' : [ 444 , 555 , 666 , 444] , 'col3': ['abc' , 'def' , 'ghi ' , 'xyz']})
df.head()
df['col2'].unique()
df['col2'].value_counts()
df[(df['col2'] >2)  & (df['col2'] == 444)]
df['col1'].sum()
def times2(x):
  return x*2
df['col1'].apply(times2)
df.drop('col1' , axis = 1)
df.sort_values('col2')
# # Data Visualization through Pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df1 = pd.read_csv('client_data.csv')
df1

# %%
df2 = pd.read_csv('data_vis.csv')
df2

# %%
df1['date_end'].hist()

# %%
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# %%
df1['date_end'].hist()

# %%
plt.style.use('ggplot')
df1['date_end'].hist()

# %%
df2.plot.area()

# %%
df2.plot.area( alpha = 0.4)

# %%
df2.head()

# %%
df2.plot.bar()

# %%
df2.plot.bar(stacked = True)

# %%
df1['cons_12m'].plot.hist()

# %%
df1.plot.scatter(x = 'date_end' , y= 'cons_12m')

# %%
df1.plot.scatter(x = 'date_end' , y= 'cons_12m' , cmap = 'coolwarm')

# %%
df2.plot.box()

# %%
df = pd.DataFrame(np.random.randn(1000, 2) , columns=  [ 'a' , 'b'])

# %%
df.head()

# %%
df2.plot.kde()


