# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:26:53 2020

@author: evinb

Use Python to create a MapReduce program to sort the total amount spent by customer
 (from the customer who spent the least to the customer who spent the most). 
 Execute. Submit your code (.py file) and output (.txt file). 
 Put your execution statement as the final line in your code (# commented out).

Hints:

You will probably need to chain two MapReduce jobs together.
Code Snippet: '%04.02f'%float(order)
This snippet allows you to change a variable
 that is a float(order) to give it leading zeros, where “order” was a float.
"""


from mrjob.job import MRJob
from mrjob.step import MRStep
from io import open

class TotalSpent(MRJob):
    def steps(self):
        
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(mapper = self.mapper_make_counts_key,
                   reducer = self.reducer_sort)
            ]
    
    def MakeNumber(self, stringtonumber):
        Number =  float(stringtonumber)
        return Number
   
    def mapper(self, _, line):
        (CustomerID,  ItemID, AmountSpent) = line.split(',')
        AmountSpent = self.MakeNumber(AmountSpent)
        yield CustomerID, AmountSpent
        

    def reducer(self, CustomerID, AmountSpent):
        yield CustomerID, sum(AmountSpent)
        
    def mapper_make_counts_key(self, AmountSpent, CustomerID ):
        yield '%04.02f'%float(CustomerID), AmountSpent


    def reducer_sort(self, CustomerID, AmountSpent):
        for c in AmountSpent:
            yield CustomerID, c

if __name__ == '__main__':
    TotalSpent.run()  
     
 # !python AmountSpentSorted.py ML3.1.csv> AmountSpentSorted.txt       
        