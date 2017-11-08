# Python program to print prime factors
 
import math
 
# A function to print all prime factors of 
# a given number n


def primefactors(n):

    if n < 2:
        primefactors(int(input("Please choose a number greater than 1: ")))
        return None
     
    # First check if number is even
    if n % 2 == 0:
        print(2)
        while n % 2 == 0:
            n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
         
        # while i divides n , print i once and divide n
        if n % i == 0:
            print(i)
            while n % i == 0:
                n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)
         
# Driver Program to test above function


num = 10
primefactors(num)
primefactors(4)
primefactors(1)
