# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:15:07 2018

@author: Polla
"""

#Sort an array by value and index
#Your task is to sort an array of integer numbers by the product of the value and the index of the positions. 
#
#For sorting the index starts at 1, NOT at 0!
#The sorting has to be ascending.
#The array will never be null and will always contain numbers. 
#
#Example:
#
#Input: 23, 2, 3, 4, 5
#Product of value and index:
#23 => 23 * 1 = 23  -> Output-Pos 4
# 2 =>  2 * 2 = 4   -> Output-Pos 1
# 3 =>  3 * 3 = 9   -> Output-Pos 2
# 4 =>  4 * 4 = 16  -> Output-Pos 3
# 5 =>  5 * 5 = 25  -> Output-Pos 5
#
#Output: 2, 3, 4, 23, 5

def sort_array(t1_array):
    my_dict_1={}
    my_dict_2={}
    result=[]
    index=1
    for i in t1_array:
        my_dict_1[index]=i
        my_dict_2[index]=i*index
        index+=1
    #print(my_dict_1)
    #print(my_dict_2)
    d_view = [ (v,k) for k,v in my_dict_2.items() ]
    d_view.sort(reverse=False)
    for v,k in d_view:
        #print ("%s: %d" % (k,v))
        #print(my_dict_1[k])
        result.append(my_dict_1[k])
    return result



t1_array=[23, 2, 3, 4, 5]
print(sort_array(t1_array))