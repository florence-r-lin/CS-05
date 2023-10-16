# CS5, hw4pr1
# Filename: hw4pr1.py
# Name: Florence Lin
# Problem description: Binary <-> decimal conversions

#1 isOdd(N)
def isOdd(N):
    """ returns True if n is odd and False is n is even
        arguments: integer N
    """
    if N%2 == 1:
        return True
    if N%2 == 0:
        return False

print("isOdd(42)    should be  False:", isOdd(42))
print("isOdd(43)    should be  True:", isOdd(43))

#2 numToBinary(N)
def numToBinary(N):
    """ converts decimal numbers into binary form one bit at a time 
        argument: N is an int
        returns a string of binary numbers
    """
    if N == 0:
        return ''
    elif N%2 == 1:
        return   (numToBinary(N//2)) + '1'
    else:
        return   (numToBinary(N//2)) + '0'
    
print("numToBinary(0)      should be  '':",  numToBinary(0))
print("numToBinary(42)     should be  '101010':",  numToBinary(42))

#3 binaryToNum(S)
def binaryToNum(S):
    """ converts string of binary numbers to a number
        argument: S is a string
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return  (binaryToNum(S[:-1])*2)  + 1

    else: # last digit must be '0'
        return   (binaryToNum(S[:-1])*2) + 0

# tests

print("binaryToNum('')     should be  0:",  binaryToNum(''))
print("binaryToNum('101010') should be  42:",  binaryToNum('101010'))


#4 increment(S)
def increment(S):
    """ accepts an 8 character string S of 0 and 1s, returns the next largest number in binary still using 8 characters
        arguments: S is an 8 character string
    """
    if S == "11111111":
        return "00000000"
    else:
        n = binaryToNum(S)
        num = n+1
        ans = numToBinary(num)
        if len(ans) < 8:
            return "0"*(8-len(ans)) + ans
        else:
            return ans
#tests
print("increment('00101001')    should be  00101010:", increment('00101001'))
print("increment('00000011')    should be  00000100:", increment('00000011'))
print("increment('11111111')    should be  00000000:", increment('11111111'))

#5 count(S,n)
def count(S, n):
    """accepts 8 character binary string as argument and counts n times upward from S and prints as it goes
    """
    if n == 0:
        print(S)
    else:
       print(S)
       S = increment(S)
       count(S,n-1)
       
    
#6 numToTernary(N)
def numToTernary(N):
    """ ternary representation of 59: 
        59/3 = 19 (2 remainder), 19/3 = 6 (remainder 1), 6/3 = 2, 2/3 = 0 (remainder 2)
        the ternary representation of the number is the remainders of the base three divison starting with 0 to 3.
        so 59 is 2012

        numToTernary(N) returns the ternary representation of N as a string
        argument: N is a decimal number
    """
    if N == 0:
        return ''
    elif N%3 == 2:
        return   (numToTernary(N//3)) + '2'
    elif N%3 == 1:
        return (numToTernary(N//3)) + "1"
    else:
        return   (numToTernary(N//3)) + '0'

#7 ternaryToNum(S)
def ternaryToNum(S):
    """ converts string of ternary numbers to a decimal number
        argument: S is a string
    """
    if S == '':
        return 0
    elif S[-1] == '2':
        return (ternaryToNum(S[:-1])*3) + 2
    elif S[-1] ==  '1':
        return (ternaryToNum(S[:-1])*3)  + 1
    else: 
        return (ternaryToNum(S[:-1])*3) + 0
    

#8 balancedTernaryToNum(S)
def balancedTernaryToNum(S):
    """ returns decimal equivalent of the balanced ternary
        argument: string of balanced ternary
    """
    if S == '':
        return 0
    elif S[-1] == '-':
        return (balancedTernaryToNum(S[:-1])*3) - 1
    elif S[-1] ==  '0':
        return (balancedTernaryToNum(S[:-1])*3) + 0
    else: 
        return (balancedTernaryToNum(S[:-1])*3) + 1
    
#9 numToBalancedTernary(N)
def numToBalancedTernary(N):
    """ balanced ternarys use + to represent +1, 0 to represent 0, and - to represent -1
        returns the balanced ternary equivalent of decimal number
        argument: N is decimal number
    """
    if N == 0:
        return ''
    elif N%3 == 2:
        N = N+3
        return   (numToBalancedTernary(N//3)) + '-'
    elif N%3 == 1:
        return (numToBalancedTernary(N//3)) + "+"
    else:
        return   (numToBalancedTernary(N//3)) + '0'


    

