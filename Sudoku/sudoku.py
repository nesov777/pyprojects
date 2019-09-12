# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:14:05 2019

@author: Oleg
"""

def sudoku():
    a = [[0, 15, 0, 5],
         [17, 0, 11, 0],
         [0, 0, 0, 0],
         [14, 9, 0, 0]]
    b = [6, 7, 8, 10, 12, 13, 16, 18, 19, 20]
    c = 0
    for i0 in range (10):
        c0 = b.copy()
        a[0][0] = c0.pop(i0)
        print ('iterate...', c0, a[0][0])
        for i1 in range (9):
            c1 = c0.copy()
            a[0][2] = c1.pop(i1)
            for i2 in range (8):
                c2 = c1.copy()
                a[1][1] = c2.pop(i2)
                for i3 in range (7):
                    c3 = c2.copy()
                    a[1][3] = c3.pop(i3)
                    for i4 in range (6):
                        c4 = c3.copy()
                        a[2][0] = c4.pop(i4)
                        for i5 in range (5):
                            c5 = c4.copy()
                            a[2][1] = c5.pop(i5)
                            for i6 in range (4):
                                c6 = c5.copy()
                                a[2][2] = c6.pop(i6)
                                for i7 in range (3):
                                    c7 = c6.copy()
                                    a[2][3] = c7.pop(i7)
                                    for i8 in range (2):
                                        c8 = c7.copy()
                                        a[3][2] = c8.pop(i8)
                                        a[3][3] = c8[0]
                                        c+=1
                                        print (c)
                                        if (sum(a[0]) == 50) and (sum(a[1]) == 50) and (sum(a[2]) == 50) and (sum(a[3]) == 50) and (list(map(sum, (zip(*a))))[0] == 50) and (list(map(sum, (zip(*a))))[1] == 50) and (list(map(sum, (zip(*a))))[2] == 50) and (list(map(sum, (zip(*a))))[3] == 50):
                                            print(a)
                                            return
sudoku()