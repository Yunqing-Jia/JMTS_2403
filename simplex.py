#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:30:10 2024

@author: jiayunqing
"""

c = [-3, -5]
A = [
    [1, 0],
    [0, 2],
    [3, 2],
]
b = [4, 12,18]

m, n = len(A), len(A[0])

tableau = [row[:] + [0] * (m+1) + [b_val] for row, b_val in zip(A, b)] #set up the initial tableau
tableau.append(c[:] + [0] * (m + 2)) #adding the objective function to the bottom row
for i in range(m+1):
    tableau[i][n + i] = 1
#print(tableau)
#print(tableau[-1][:-1])
#basic_vari_index=[5,6,7,8] 
basic_vari_index=list(range(n + 1, n + m + 1)) #identified the basic variables corresponding to the slack variables
print(basic_vari_index)

while min(tableau[-1][:-1]) < 0:
    pivot_col = tableau[-1][:-1].index(min(tableau[-1][:-1])) #selected the pivot column with the most negative coefficient
    ratios = [(tableau[i][-1] / tableau[i][pivot_col], i) for i in range(m) if tableau[i][pivot_col] > 0]
    pivot_row = min(ratios)[1] #determined the pivot row
    
    pivot_element = tableau[pivot_row][pivot_col] #selecting the pivot element
    tableau[pivot_row] = [x / pivot_element for x in tableau[pivot_row]] #normalized the pivot row
    
    basic_vari_index[pivot_row]=pivot_col+1 #updates the basic variable indices
    print(basic_vari_index)
    
    for i in range(len(tableau)):   #adjusted the other rows to maintain feasibility
        if i != pivot_row:
            ratio = tableau[i][pivot_col]
            tableau[i] = [tableau[i][j] - ratio * tableau[pivot_row][j] for j in range(len(tableau[i]))]
            
            
b_final=[tableau[i][-1] for i in range(m)]
solution = [0] * (m+n+1)
for i in range(len(basic_vari_index)):
    solution[basic_vari_index[i]] = b_final[i]
    
    
print("x_optimal:", solution[1:n+1])
print("f_optimal:", -tableau[-1][-1])