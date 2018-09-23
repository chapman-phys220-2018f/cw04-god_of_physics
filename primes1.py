#!/usr/bin/env python3
 #-*- coding: utf-8 -*-
import sys 
import math 
n = int(sys.argv[1]) 

def gen_eratosthenes():
    a = 1
    b = 1
    while True:
 #   for _ in range(n):
        yield b
        a , b = b , a + b
#print(list(fib_gen(a)))

def eratosthenes(n):
    if (n >= 3):
    a = 1
        list1 = []
    b = 1

        f = gen_eratosthenes()
        for i in range(n):
    while True:
            list1.append(( i + 1 ))
 #   for _ in range(n):
        a = 2
        yield b
        for x in range(int(math.ceil(math.sqrt(n)))):
        a , b = b , a + b
            for i in list1:
                if ( i != a and ( i % a == 0 ) and i > 1):
                    list1.remove(i)
            a = a + 1
        del list1[0]
        print list1


  
  else:
        print("There are no primes less than your number.")
eratosthenes(n)

