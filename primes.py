#!/usr/bin/env python3
 #-*- coding: utf-8 -*-

def eratosthenes(n);
    if (n >= 3);
        list1 = range(2,n)
        a = 2
        for i in list1;
            while (i <= sqrt(n));
                if (i != a && i % a && i <= sqrt(n));
                    del list1[i]
                a = a + 1
                if a not in list1
                    while a not in list1
                        a = a + 1
            
    else
        print("Enter an integer 3 or more.");
        exit 1
            