# # Matplotlib & Seaborn Function
# - Matplotlib is a low level graph plotting library in python (for visualization)
# - It was  created by john D.Hunter
# - Open source 
# - Free 
import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(0 ,5 ,11)

y = x**2
x
y

p1 = plt.plot(x , y , 'r')
print(p1)

# # Seaborn 
# - Seaborn is library that uses Matplotlib underneath to plot graphs
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution plot
tips = sns.load_dataset('tips')
tips.head()

# Data Vsualization
sns.distplot(tips['total_bill'])

sns.distplot(tips['total_bill'] , kde = False , bins = 30)

sns.jointplot(x= 'total_bill' , y = 'tip' , data = tips)

sns.jointplot(x= 'total_bill' , y = 'tip' , data = tips , kind = 'reg')

sns.jointplot(x= 'total_bill' , y = 'tip' , data = tips , kind = 'kde')

sns.pairplot(tips)

sns.pairplot(tips , hue = 'smoker')

sns.rugplot(tips ['total_bill'])

# # Categorical plot
sns.load_dataset('tips')
tips.head()


import numpy as np

# sns.barplot( x = ' total_bill' , y = ' tip' , data = tips , estimator=np.std)
sns.countplot(x = 'total_bill' , data= tips)

sns.boxplot(x = 'day' , y = ' total_bill' , data=tips)

sns.violinplot(x= 'day' , y = 'total_bill' , data = tips , hue = 'sex')

sns.violinplot(x= 'day' , y = 'total_bill' , data = tips , hue = 'sex' , split = True)

# sns.stripplot(x = 'day' , y = ' total_bill' , data = tips)
sns.stripplot(x = 'day' , y = 'total_bill' , data= tips , hur = 'sex')

sns.stripplot(x = 'day' , y = 'total_bill' , data= tips , hur = 'sex' , jitter = True , spli = True)

sns.swarmplot(x = 'day' , y = 'total_bill' , data = tips )

sns.violinplot(x = 'day' , y = 'total_bill' , data= tips)

sns.swarmplot(x = 'day' , y= 'total_bill' , data =tips , color = 'black' , size = 3)

# # Matrix Plot

import seaborn as sns
flight = sns.load_dataset('flights')

flight.head()

tips = sns.load_dataset('tips')
tips.head()

tips.corr()
sns.heatmap(tips.corr() , cmap= 'coolwarm' , annot = True)

fp = flight.pivot_table(values = 'passengers' , index = 'month' , columns = 'year')
fp
sns.heatmap(fp)

import matplotlib as plt
import seaborn as sns
Iris = sns.load_dataset('iris')

Iris.head()

tips = sns.load_dataset('tips')
tips.head()

sns.set_style('white')
sns.countplot(x = 'smoker' , data= tips)

sns.set_style('white')
# palette means to light the color 
sns.countplot(x = 'smoker' , data= tips  , palette = 'deep')

sns.set_style('white')
sns.countplot(x = 'smoker' , data= tips)
# remove the lines 
sns.despine(left = True)

import matplotlib as plt

# plt.figure(figsize = (12 , 3))
# sns.countplot( x = 'smoker' , data = tips)

sns.lmplot( x = 'total_bill' , y = 'tip' , size = 2  , aspect = 4  , data= tips)


sns.set_context('poster') 
sns.countplot(x = 'smoker ' , data=tips , palette = ' coolwarm')
