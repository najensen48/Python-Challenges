#Using the following data on the top baseball salary in the National and American league -https://www.baseball-reference.com/leaders/Salary_leagues.shtml. 
#The values in the columns, are 'year', 'NL top salary', 'AL top salary'

data=[[2019, 42143000, 36833333], 
      [2018, 35571429, 34083000], 
      [2017, 35571429, 30000000], 
      [2016, 34571429,30000000,], 
      [2015, 32571429, 28000000]]

#1. Create a Pandas Array
#2. Write a function to determine (and return) the increase in both NL salaries and in AL salaries in the last 5 years.
#3. Write a function to determine (and return) the difference between the NL and the AL top salary in each of the last 5 years.

#SOLUTIONS

import pandas as pd

data=[[2019, 42143000,36833333], 
      [2018, 35571429, 34083000], 
      [2017, 35571429,30000000], 
      [2016, 34571429,30000000,], 
      [2015, 32571429, 28000000]]


#1. Create a Pandas Array
pd_baseball = pd.array(data)
print(pd_baseball)
print(type(pd_baseball))

#RETURN
[[    2019 42143000 36833333]
 [    2018 35571429 34083000]
 [    2017 35571429 30000000]
 [    2016 34571429 30000000]
 [    2015 32571429 28000000]]
<class 'numpy.ndarray'>

#2. Write a function to determine (and return) the increase in both NL salaries and in AL salaries in the last 5 years.
import pandas as pd
df=pd.DataFrame(data)
print(df)
df_cust = pd.DataFrame(data, columns=['year', 'NL top salary', 'AL top salary'])
print(df_cust)
print("-------------THE PERCENTAGES---------")
nl_increase = (((df_cust['NL top salary'][0]-df_cust['NL top salary'][4])/df_cust['NL top salary'][4])*100)
print(nl_increase,"%","This is the increase in NL salaries")
al_increase = (((df_cust['AL top salary'][0]-df_cust['AL top salary'][4])/df_cust['AL top salary'][4])*100)
print(al_increase,"%","This is the increase in AL salaries")

#RESULT
 0         1         2
0  2019  42143000  36833333
1  2018  35571429  34083000
2  2017  35571429  30000000
3  2016  34571429  30000000
4  2015  32571429  28000000
   year  NL top salary  AL top salary
0  2019       42143000       36833333
1  2018       35571429       34083000
2  2017       35571429       30000000
3  2016       34571429       30000000
4  2015       32571429       28000000
-------------THE PERCENTAGES---------
29.386401806319274 % This is the increase in NL salaries
31.547617857142857 % This is the increase in AL salaries


#3. Write a function to determine (and return) the difference between the NL and the AL top salary in each of the last 5 years.
year_2019 = (df_cust['NL top salary'][0]-df_cust['AL top salary'][0])
year_2018 = (df_cust['NL top salary'][1]-df_cust['AL top salary'][1])
year_2017 = (df_cust['NL top salary'][2]-df_cust['AL top salary'][2])
year_2016 = (df_cust['NL top salary'][3]-df_cust['AL top salary'][3])
year_2015 = (df_cust['NL top salary'][4]-df_cust['AL top salary'][4])
salary_difference = [year_2019,year_2018,year_2017,year_2016,year_2015]
df_cust['salary difference'] = salary_difference
print(df_cust)


#RESULT
year  NL top salary  AL top salary  salary difference
0  2019       42143000       36833333            5309667
1  2018       35571429       34083000            1488429
2  2017       35571429       30000000            5571429
3  2016       34571429       30000000            4571429
4  2015       32571429       28000000            4571429

