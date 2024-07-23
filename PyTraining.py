from math import * ; import math
from random import * ; import random
from secrets import * ; import secrets 
from sys import * ; import sys 
from calendar import * ; import calendar
from time import * ; import time
from functools import * ; import functools 

def SpeedUp(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache: cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def TimeIt(func, num_times: int = 1_000_000, *args, **kwargs) -> str:
    s: float = time.perf_counter()
    for _ in range(num_times): func(*args, **kwargs)
    e: float = time.perf_counter()
    return f'\nTime: {(e - s):.6f} seconds.'

# def PrintTest() -> None: print(TimeIt(fib, eval(input('Enter number of times: ')), int(input('Enter Symbol: '))))

# prime_digits = {2, 3, 5, 7}
# # characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$&' 

# # fl = 6.969
# # print("%.1f"%fl)

# Odd_or_Even_WA = lambda x: "Even" if str(bin(int(x))).endswith('0') else "Odd" 

# Odd_or_Even_WOA = lambda : "Even" if str(num := bin(int(input(': ')))).endswith('0') else "Odd"    

# def printstr(x): stdout.write(x) 

# @SpeedUp
# def fib(x: int = 0) -> int: 
#     if x == 0: return 0
#     elif x == 1: return 1
#     y, z = 0, 1
#     for _ in range(2, x + 1): y, z = z, y + z
#     return z

# def fibonacci(x) -> None: 
#     a, b = 0, 1
#     for _ in range(x): print(a, end = ' ') ; a, b = a + b, a

# def ispalindrome(x) -> bool:
#     x.lower()
#     x = "".join(_ for _ in x if _.isalnum()) 
#     return x == x[::-1]

# def GCD(x, y) -> int:
#     A = B = S = []
#     for _ in range(1, x + 1): 
#         if x % _ == 0: A.append(_) 
#     for _ in range(1, y + 1):
#         if y % _ == 0: B.append(_) 
#     for _ in (A + B):
#         if _ in (A + B): S.append(_) 
#     return max(S)

# def isprime(x) -> bool: 
#     if x < 2: return False
#     for _ in range(2, int(x**0.5) + 1): 
#         if x % _ == 0: return False 
#     return True

# def factors_num(x) -> list:
#     A : list = []
#     for _ in range(1, x):
#         if x % _ == 0: A.append(_)
#     return A

# def randstr(x) -> str:
#     R_S : str
#     for _ in range(x): R_S += secrets.choice(characters)
#     print(R_S) 

# def isodd(x) -> bool: return True if x / 2 != x // 2 else False

# def iseven(x) -> bool: return True if x / 2 == x // 2 else False    

# def swap(x, y): return y, x

# def rotateleft(): 
#     a, x, b = list(map(int, input(": ").split())), int(input(": ")), None 
#     b = a[len(a) - x:] + a[:len(a) - x] 
#     print(b)

# def rotateright(): 
#     a , x = list(map(int, input(": ").split())), int(input(": ")) ; b = None 
#     b = a[x:] + a[:x]
#     print(b)

# def isArmstrong(x) -> bool: 
#      a = [pow(_, len(str(x))) for _ in list(map(int, str(x)))]
#      if x == sum(a): return True
#      else: return False

# def getvowels() -> str:
#     V : str = str()
#     for _ in range(65, 123): 
#         if chr(_) in "aeiouAEIOU": V += chr(_)
#     return V    

# def getconsonants() -> str:
#     C : str = str()
#     for _ in range(65, 123):
#         if (chr(_) not in "aeiouAEIOU") and (chr(_).isalpha()): C += chr(_)
#     return C    

# def is_leap_year(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0: return True
#       else: return False
#     else: return True
#   else: return False

# def ismagic1(x):
#     sum : int = 0
#     while x > 0 or sum > 9:
#         if x == 0:
#             x = sum
#             sum = 0
#         sum += x % 10
#         x //= 10
#     return sum == 1

# def ismagic2(x):
#     s : int = 0
#     for _ in str(x):
#         if _.isdigit(): s += int(_)
#     t = str(s)
#     r = t[::-1]
#     return True if x == s * int(r) else False

# def isautomorphic(x): 
#     return True if str(x ** 2).endswith(str(x)) else False

# def isharshad(x):
#     s : int = 0
#     for _ in str(x):
#         if _.isdigit(): s += int(_)
#     return True if x % s == 0 else False    

# def isabundant(x):
#     fact : list = []
#     for i in range(1, x):
#         if x % i == 0: fact.append(i)
#     return True if x < sum(fact) else False

# vowels = getvowels()
# consonants = getconsonants() 
 
# # 1. programme to cheque whether the given number is even or odd 
# def one(): print("Odd!" if int(input(": ")) & 1 != 0 else "Even!")

# # 2. Max of two numbers
# def two(): print("Max of two numbers is :",max(list(map(int,input("Enter two values: ").split()))))

# # 3. Max of three numbers 
# def three(): print("Max of 3 numbers is :",max(list(map(int,input("Enter 3 values: ").split())))) 

# # 4. Max 4 numbers
# def four(): print("Max of 4 numbers is :",max(list(map(int,input("Enter 4 values: ").split()))))

# # 5. Sum of n natural numbers
# def five(): 
#     a = int(input(": ")) 
#     print(a * (a + 1) // 2)

# # 6. Factorial of a given number
# def six(): print(factorial(int(input(": "))))

# # 7. Extracting digits from the given number
# def seven():
#     s = input(": ")
#     for _ in s: 
#         if _.isdigit(): print(_)

# # 8. Count number of digits present in the given number
# def eight(): print(len(x for x in input(': ') if x.isdigit()))

# # 9. Check whether the given digit is present in a number or not
# def nine(): print(input("Digit: ") in input("Num: ")) 

# # 10. Reverse the given number
# def ten():
#     a = input(": ") ; n = int(a)
#     while n != 0:
#         d = n % 10
#         print(d, end = '')
#         n //= 10

# # 11. Number of trailing zeros in factorial of the given number.
# def eleven():
#     a = factorial(int(input(": "))) ; count = 0 ; print(a)
#     while a != 0:
#         rem = a % 10
#         if rem == 0: count += 1
#         else: break
#         a //= 10 
#     print(count)    

# # 12. Implement a program to find X to the power of Y
# def twelve(): print(input("X: ") ** input("Y: "))

# # 13. Sum of digits of a given number
# def thirteen():
#     a = input(": ") ; sum = 0
#     for _ in a: sum += int(_)
#     print(sum)

# # 14. Sum of the odd digits of a given number
# def fourteen():
#     a = input(": ") ; sum = 0 
#     for _ in a:
#         if isodd(int(_)): sum += int(_) 
#     print(sum)    

# # 15. Sum of prime digits in a given number
# def fifteen():
#     a = input(": ") ; sum = 0
#     for _ in a:
#         if int(_) in primes: sum += int(_) 
#     print(sum) 

# # 16. Factors of a given number
# def sixteen():
#     a = int(input(": ")) ; factors = [] 
#     for _ in range(1, a):
#         if a % _ == 0: factors.append(_) 
#     print(factors)    

# # 17. Display all the prime numbers between range
# def seventeen():
#     a, b = int(input("A: ")), int(input("B: ")) ; primes = []
#     for _ in range(a, b+1):
#         if isprime(_): primes.append(_)
#     print(primes)    

# # 18. Display the count of all the prime numbers between range
# def eighteenth():
#     a, b = int(input("A: ")), int(input("B: ")) ; primes, count= [], 0
#     for _ in range(a, b+1):
#         if isprime(_): primes.append(_)
#     count += 1
#     print(primes, count)
    
# # 19. Check whether a given number is a palindrome or not
# def nineteen():
#     a = input(": ").lower()
#     a = "".join(_ for _ in a if _.isalnum()) 
#     print(a == a[::-1])
    
# # 20. Check whether a given number is a Armstrong number or not
# def twenty():
#     a = input(": ") 
#     if int(a) == sum(pow(_, len(a)) for _ in list(map(int, a))): print("Armstrong number!")
#     else: print("Not a Armstrong number!")

# # 21. Check whether a given number is a Strong number or not
# def twentyone():
#     a = input(": ") 
#     if int(a) == sum(factorial(_) for _ in list(map(int, a))): print("Strong number!")
#     else: print("Not a Strong number!") 
    
# # 22. Check whether a given number is a Perfect number or not
# def twentytwo():
#     a = input(": ") 
#     if int(a) == sum(factors_num(int(a))): print("Perfect number!")
#     else: print("Not a perfect number!")
    
# # 23. Addition without any operators
# def twentythree():
#     a, b = int(input(": ")), int(input(": "))
#     while b:
#         c = a & b
#         a = a ^ b
#         b = c << 1
#     print(a)

# # 24. Count the number of Armstrong numbers between a range
# def twentyfour():
#     A = []
#     for _ in range(int(input(": ")), int(input(": ")) + 1):
#         if isArmstrong(_): A.append(_)
#     print(A)     

# # 25. Happy Number or not
# def twentyfive(): print(ishappy(input(": ")))

# # 26. Character Frequency
# def twentysix():
#     a = input(": ") 
#     count = {_: a.count(_) for _ in (set(a))}
#     print(count) 
    
# # 27. Vowel Frequency
# def twentyseven():
#     print(sum(1 for _ in input(": ") if _ in set('aeiouAEIOU')))

# # 28. Consonant Frequency
# def twentyeight(): 
#     print(sum(1 for _ in input(": ") if _ not in set('aeiouAEIOU')))

# # 29. Magic Number
# def twentynine(): print(ismagic(int(input(": "))))

# # 30. Replace the frequent character
# def thirty(): 
#     a, b = input("String: ").lower(), input("X: ") 
#     F_C, M_F = None,  0 
#     for _ in a: 
#         C = a.count(_) 
#         if C > M_F: F_C = _ , M_F = C 
#     print(a.replace(F_C, b).title())

# # 31. Patterns 
# class thirtyone():
    
#     def __init__(self): pass
    
#     def diamond(self): 
#         a = int(input(": "))
#         for _ in range(a): print(" " * (a - _ - 1) + "*" * (2 * _ + 1))
#         for _ in range(a - 2, -1, -1): print(" " * (a - _ - 1) + "*" * (2 * _ + 1))
    
#     def alpha_floyd(self): 
#         x = 1 
#         a = int(input(": "))
#         for _ in range(65, (65+a)): print(chr(_) * x) ; x += 1 

#     def floyd(self):
#         x = 1
#         a = int(input(": "))
#         for _ in range(1, a + 1): 
#             for i in range(1, _ + 1): print(x, end = " ") ; x += 1 
#             print() 

# # 32. Recursions
# class recursions():
    
#     def __init__(self): pass 
    
#     def fib(self, x): 
#         if x == 0: return 0
#         elif x == 1: return 1
#         else: return self.fib(x - 1) + self.fib(x - 2)  
        
#     def power(self, x, y):
#         if y == 0: return 1
#         elif y == 1: return x
#         else: return self.power(x, y-1) * x
        
#     def rev_num(self, x, l): 
#         if x == 1: return x
#         else: return (x % 10) * (10 ** (l - 1)) + self.rev_num(x // 10, l - 1) 
    
#     def ishappy(self, x):
#         if len(str(x)) == 1: return True if x in [1, 7] else False
#         else:
#              s = 0 
#              while x: r = x % 10 ; s += (r**2) ; x //= 10
#              return self.ishappy(s)   

#     def ismagic(self, x):
#         if len(str(x)) == 1: return True if x == 1 else False
#         else: 
#             s = 0
#             while x: r = x % 10 ; s += r ; x //= 10 
#             return self.ismagic(s) 

# # 33. Remove Duplicates
# def thirtythree():
#     a = list(map(int, input(": ").split()))
#     print(set(a))

# # 34. Sum of even elements of a list
# def thirtyfour():
#     a = list(map(int, input(": ").split())) ; b = None
#     for _ in a:
#         if iseven(a[_]): b += a[_]
#     print(b)
    
# # 35. sum of odd elements of a list
# def thirtyfive():
#     a = list(map(int, input(": ").split())) ; b = None
#     for _ in a:
#         if isodd(a[_]): b += a[_]
#     print(b)
    
# # 36. Seperate even and odd elements of a list
# def thirtysix():
#     a = list(map(int, input(": ").split())) ; b, c = None, None
#     for _ in a:
#         if isodd(a[_]): b.append(a[_])
#         else: c.append(a[_])
#     print(b, c)
    
# # 37. Count elements of a list
# def thirtyseven():
#     a = list(map(int, input(": ").split()))
#     print(len(a))
    
# # 38. Sum of elements of a list
# def thirtyeight():
#     a = list(map(int, input(": ").split()))
#     print(sum(a))
    
# # 39. Minimum element of a list
# def thirtynine():
#     a = list(map(int, input(": ").split()))
#     print(min(a))
    
# # 40. Maximum element of a list
# def forty():
#     a = list(map(int, input(": ").split()))
#     print(max(a))
    
# # 41. Left Rotate list
# def fortyone(): rotateleft() 
    
# # 42. Right Rotate list
# def fortytwo(): rotateright()

# # 43. Turn list into matrix
# def fortythree():
#     a = list(map(int, input(": ").split()))
#     print(array(a).reshape(3, 3))
    
# # 44. Trace of matrix
# def fortyfour():
#     a = list(map(int, input(": ").split()))
#     b = array(a).reshape(3, 3)
#     print(b, trace(b))
    
# # 45. Matrix without NumPy
# def fortyfive():
#     print() ; dimension = int(input("Enter dimensions: "))
#     rows = cols = dimension

#     print() ; print("Enter Matrix:")
#     a = [[int(input(": ")) for _ in range(cols)] for _ in range(rows)] ; print()

#     print("Matrix:")
#     for i in range(rows):
#         for j in range(cols): print(a[i][j], end=" ")
#         print()
#     print()
    
#     print("Transpose of Matrix:")
#     for i in range(rows):
#         for j in range(cols): print(a[j][i], end=" ")
#         print()
#     print()
    
#     print("Diagonal:")
#     trace = 0
#     for i in range(rows):
#         trace += a[i][i]
#         print(a[i][i], end=" ")
#     print("\nThe Trace is:", trace) ; print()

#     print("Inverse Diagonal:")
#     inv_trace = 0
#     for i in range(dimension):
#         inv_trace += a[i][dimension - i - 1]
#         print(a[i][dimension - i - 1], end=" ")
#     print("\nInverse trace is:", inv_trace) ; print()

#     # Row sum
#     for j in range(dimension):
#         r_sum = 0
#         print("Row", j + 1, end=": ")
#         for i in range(cols):
#             r_sum += a[j][i]
#             print(a[j][i], end=" ")
#         print("\nRow sum:", r_sum) ; print()

#     # Column sum
#     for j in range(dimension):
#         c_sum = 0
#         print("Column", j + 1, end=": ")
#         for i in range(rows):
#             c_sum += a[i][j]
#             print(a[i][j], end=" ")
#         print("\nColumn sum:", c_sum) ; print()

#     # Matrix square
#     b = a @ a  
#     print(f'Matrix Square is {b}') ; print()
        
#     # Matrix sum
#     m_sum = sum(sum(row) for row in a)
#     print("Matrix sum:", m_sum) ; print()

# # 46. Flatten a Shallow List 
# def fortysix():
#     a = eval(input()) ; b = []
#     for _ in a:
#         if isinstance(_, list): b.extend(_)
#         else: b.append(_)
#     return b 

# # 47. 
# def fortyseven(): 
#     a = input()
#     b = {_: a.count(_) for _ in a}
#     return b

# # 48.
# def fortyeight():
#     a = eval(input())
#     b = eval(input())
#     c = eval(input())
#     return {**a, **b, **c}

# # 49. 
# def fortynine(x):
#     a = 2 ** x + 1
#     b = 2 * x + 1
#     return True if a % b == 0 else False 

# 50. 
def getmethods(module: str | None) -> None:
    if module is None: print('No module specified!') 
    else: 
        try:
            module = __import__(module)
            print('Do you want to see the dunder methods for this module?')
            _ = input("Yes or No (Y/N): ")
            if _.upper() == 'Y':
                for i, method in enumerate(dir(module), start = 1): print(i, method, sep=': ') 
                return
            else:
                for i, method in enumerate(dir(module), start = 1):
                    if not method.startswith('__'): print(i, method, sep=': ')
                return    
        except ImportError: 
            print(f'Module {module} might not exist!\nOr 🤔\nIt is not specified/installed yet!')
            print('Do you want to continue? (Y/N): ')
            if _.upper() == 'Y': getmethods("Enter Module: ")
            else: return 
    
# # 51. SwapNibbles
# SwapNibbles = lambda x = 0: ((x & 0xF0) >> 4) | ((x & 0x0F) << 4)

randomListGenerator = lambda a, b, c: \
  list(random.randrange(a, b, c) for i in range(int(input("Length of List: "))))

  

def main():
    # sys.setrecursionlimit(10_000)
    getmethods(input("Enter Module: "))

if __name__ == '__main__': main()