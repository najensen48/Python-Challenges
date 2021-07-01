#The 'yahoo' data source is recommended for this problem. Use source='yahoo'

#1. Use pandas datareader and the datetime library to pull data for the last two months of Google stock values. Create a pandas data frame of the values.
#2. Use a built-in pandas.DataFrame function or write your own function to generate a statistical summary of the data that includes, at least the count, mean, and standard deviation.
#3. Complete the code to find the percentage of days on which the stock closed higher than it opened.
#4. Use the pandas.DataFrame pct_change() function to determine the percent change in opening price.
#5. Use a visualization library to create a lineplot of the closing price over the last year.

#SOLUTIONS
import pandas_datareader.data as web
from pandas_datareader import data, DataReader
from datetime import datetime
import seaborn as sns
import numpy as np

#1. Use pandas datareader and the datetime library to pull data for the last two months of Google stock values. Create a pandas data frame of the values.
start = datetime(2021,2,1)
end = datetime(2021,3,31)
googl = web.DataReader('GOOGL','yahoo', start, end)
print(googl.head(4))

#2. Use a built-in pandas.DataFrame function or write your own function to generate a statistical summary of the data that includes, at least the count, mean, and standard deviation.
googl.describe()

#3. Complete the code to find the percentage of days on which the stock closed higher than it opened.
googl['Up']=np.where(googl['Close']>googl['Open'],1,0)
googl.head(4)
googl['Up'].sum()/googl['Up'].count()

#4. Use the pandas.DataFrame pct_change() function to determine the percent change in opening price.
googl['Close'].pct_change()

#5. Use a visualization library to create a lineplot of the closing price over the last year.
import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(googl['Close'])
googl.head()


#RESULTS
                   High          Low  ...   Volume    Adj Close
Date                                  ...                      
2021-02-01  1915.540039  1844.589966  ...  2012600  1893.069946
2021-02-02  1949.369995  1906.369995  ...  3316600  1919.119995
2021-02-03  2106.620117  2013.550049  ...  4894100  2058.879883
2021-02-04  2069.300049  2035.099976  ...  2429800  2053.629883

[4 rows x 6 columns]
High	Low	Open	Close	Volume	Adj Close	Up
Date							
2021-02-01	1915.540039	1844.589966	1844.589966	1893.069946	2012600	1893.069946	1
2021-02-02	1949.369995	1906.369995	1913.130005	1919.119995	3316600	1919.119995	1
2021-02-03	2106.620117	2013.550049	2065.610107	2058.879883	4894100	2058.879883	0
2021-02-04	2069.300049	2035.099976	2060.620117	2053.629883	2429800	2053.629883	0
2021-02-05	2095.939941	2050.000000	2059.560059	2088.830078	1489700	2088.830078	1
