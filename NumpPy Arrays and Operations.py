#Using the following data on the top baseball salary in the National and American league -https://www.baseball-reference.com/leaders/Salary_leagues.shtml. 
#The values in the columns, are 'year', 'NL top salary', 'AL top salary'

data=[[2019, 42143000, 36833333], 
      [2018, 35571429, 34083000], 
      [2017, 35571429, 30000000], 
      [2016, 34571429,30000000,], 
      [2015, 32571429, 28000000]]
#1. Create a NumPy Array
#2. Write a function to determine (and return) the increase in both NL salaries and in AL salaries in the last 5 years.
#3. Write a function to determine (and return) the difference between the NL and the AL top salary in each of the last 5 years.

#SOLUTIONS

#1. Create a NumPy Array
import numpy as np

data=[[2019, 42143000,36833333], 
      [2018, 35571429, 34083000], 
      [2017, 35571429,30000000], 
      [2016, 34571429,30000000,], 
      [2015, 32571429, 28000000]]
np_baseball = np.array(data)
print(np_baseball)
print(type(np_baseball))

#RETURN
[[    2019 42143000 36833333]
 [    2018 35571429 34083000]
 [    2017 35571429 30000000]
 [    2016 34571429 30000000]
 [    2015 32571429 28000000]]
<class 'numpy.ndarray'>

#2. Write a function to determine (and return) the increase in both NL salaries and in AL salaries in the last 5 years.

nl_increase= (((np_baseball[0][1]-np_baseball[4][1])/np_baseball[4][1])*100)
print(nl_increase, "%", "This is the increase in NL salaries")
al_increase= (((np_baseball[0][2]-np_baseball[4][2])/np_baseball[4][2])*100)
print(al_increase,"%","This is the increase in AL salaries")

#RETURN
29.386401806319274 % This is the increase in NL salaries
31.547617857142857 % This is the increase in AL salaries

#3. Write a function to determine (and return) the difference between the NL and the AL top salary in each of the last 5 years.

print("THE NEW COLUMN IS THE DIFFERENCE BETWEEN THE SALARIES FOR THAT YEAR")

year_2019 = (np_baseball[0][1]-np_baseball[0][2])
year_2018 = (np_baseball[1][1]-np_baseball[1][2])
year_2017 = (np_baseball[2][1]-np_baseball[2][2])
year_2016 = (np_baseball[3][1]-np_baseball[3][2])
year_2015 = (np_baseball[4][1]-np_baseball[4][2])
new_column = [[year_2019],[year_2018],[year_2017],[year_2016],[year_2015]]
np_baseball = np.append(np_baseball,new_column,axis=1)
print(np_baseball)

#RETURN
THE NEW COLUMN IS THE DIFFERENCE BETWEEN THE SALARIES FOR THAT YEAR
[[    2019 42143000 36833333  5309667]
 [    2018 35571429 34083000  1488429]
 [    2017 35571429 30000000  5571429]
 [    2016 34571429 30000000  4571429]
 [    2015 32571429 28000000  4571429]]
