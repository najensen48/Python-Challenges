{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data manipulation with Numpy and Pandas\n",
    "\n",
    "Test"
  },#Problem 1: String Operations
#Write a function that accepts a string of the form:

'$45.21,$62.15,$565.02,$789.98'
#and splits it into a list of floats with no $ symbols. Given the string above as an input, the program should return:

[45.21, 62.15, 565.02, 789.98]
#and have a list data type.

#SOLUTION
data='$45.21,$62.15,$565.02,$789.98'
  
def no_money(string):
  string = string.replace("$","")
  res = [float(idx) for idx in string.split(',')]
  return res
print(no_money(data))

#RESULTS
[45.21, 62.15, 565.02, 789.98]
