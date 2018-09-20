#!/usr/bin/env python3
 #-*- coding: utf-8 -*-
import sys

n = int(sys.argv[1])

def eratosthenes(n):
    if (n >= 3):
        list1 = []
        for i in range(n):
            list1.append(i)
        a = 2
        for i in list1.len:
            for i in range(n):
                if (i != a and (i % a == 0)):
                    del list1[i]
            a = a + 1
            if a not in list1:
                 while a not in list1:
                    a = a + 1
        print list1

    else:
        print("Enter an integer 3 or more.")

eratosthenes(n)