#Problem 2: Data Structures 
#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
#You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. 
#Write a function called profit() that returns the total profit made, rounded to the nearest dollar.

#Example:

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030

#Assume all inventory is sold.
#Use Profit = Total Sales - Total Cost

#SOLUTION
def profit(adictionary):
    profit = int((adictionary['sell_price'] - adictionary['cost_price']) * adictionary['inventory'])
    return profit
#Test:
result=profit({
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
     })
print(result, type(result))

#RETURN
44030 <class 'int'>
