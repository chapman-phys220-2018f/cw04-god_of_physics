#!/usr/bin/env python3
 #-*- coding: utf-8 -*-
import sys
import math

n = int(sys.argv[1])

def eratosthenes(n):
    if (n >= 3):
        list1 = []
        for i in range(n):
            list1.append(( i + 1 ))
        a = 2
        for x in range(int(math.ceil(math.sqrt(n)))):
            for i in list1:
                if ( i != a and ( i % a == 0 ) and i > 1):
                    list1.remove(i)
            a = a + 1
        del list1[0]
        print list1

    else:
        print("There are no primes less than your number.")

eratosthenes(n)