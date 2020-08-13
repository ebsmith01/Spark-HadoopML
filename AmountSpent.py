# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:35:23 2020

@author: evinb

For this assignment, you will work with data in a CSV filePreview the document.
 Before you begin, here are a few things to know about this data:

The rows are Orders.
The first column is Customer ID Number, the second column is Item ID Number, 
and the third column is Amount Spent on the Order.
Note that Customer ID Number and Item ID Number repeat 
(i.e., a customer will have multiple orders, and an item will be ordered more than once).
Your objective for this assignment, outlined below, has two parts.

Your Objective
Part 1:

Use Python to create a MapReduce program to determine the total amount spent by customer.
 Execute. Submit your code (.py file) and
 output (.txt file). Put your execution statement as the final line in your code (# commented out).
"""

from mrjob.job import MRJob
from mrjob.step import MRStep
from io import open

class TotalSpent(MRJob):
    
    def MakeNumber(self, stringtonumber):
        Number =  float(stringtonumber)
        return Number
   
    def mapper(self, _, line):
        (CustomerID,  ItemID, AmountSpent) = line.split(',')
        AmountSpent = self.MakeNumber(AmountSpent)
        yield CustomerID, AmountSpent
        

    def reducer(self, CustomerID, AmountSpent):
        yield CustomerID, sum(AmountSpent)
 

if __name__ == '__main__':
    TotalSpent.run()  
     
 # !python AmountSpent.py ML3.1.csv> AmountSpent.txt       
        