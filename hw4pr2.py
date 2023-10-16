#hw4pr2.py
# Florence Lin

#function 1 numToBaseB(N, B)
def numToBaseB(N, B):
    """ convert from decimal number N to base B
        arguments: N is a non negative integer and B is an integer between 2 and 10
    """
    if N == 0:
        return ''
    elif N%B == 1:
        return   (numToBaseB(N//B, B)) + '1'
    elif N%B == 2:
        return   (numToBaseB(N//B, B)) + '2'
    elif N%B == 3:
        return   (numToBaseB(N//B, B)) + '3'
    elif N%B == 4:
        return   (numToBaseB(N//B, B)) + '4'
    elif N%B == 5:
        return   (numToBaseB(N//B, B)) + '5'
    elif N%B == 6:
        return   (numToBaseB(N//B, B)) + '6'
    elif N%B == 7:
        return   (numToBaseB(N//B, B)) + '7'
    elif N%B == 8:
        return   (numToBaseB(N//B, B)) + '8'
    elif N%B == 9:
        return   (numToBaseB(N//B, B)) + '9'
    else:
        return   (numToBaseB(N//B, B)) + '0'
    
assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'

#function 2 baseBToNum(S, B)
def baseBToNum(S, B):
    """ returns an integer that represents the string in base B
        arguments: S is a string, B is the base between 2 and 10 inclusive
    """
    if S == '':
        return 0
    elif S[-1] ==  '9':
        return  (baseBToNum(S[:-1], B)*B)  + 9
    elif S[-1] ==  '8':
        return  (baseBToNum(S[:-1], B)*B)  + 8
    elif S[-1] ==  '7':
        return  (baseBToNum(S[:-1], B)*B)  + 7
    elif S[-1] ==  '6':
        return  (baseBToNum(S[:-1], B)*B)  + 6
    elif S[-1] ==  '5':
        return  (baseBToNum(S[:-1], B)*B)  + 5
    elif S[-1] ==  '4':
        return  (baseBToNum(S[:-1], B)*B)  + 4
    elif S[-1] ==  '3':
        return  (baseBToNum(S[:-1], B)*B)  + 3
    elif S[-1] ==  '2':
        return  (baseBToNum(S[:-1], B)*B)  + 2
    elif S[-1] ==  '1':
        return  (baseBToNum(S[:-1], B)*B)  + 1
    else: 
        return   (baseBToNum(S[:-1], B)*B) + 0
    
#function 3 baseToBase(B1, B2, s_in_B1)
def baseToBase(B1, B2, s_in_B1):
    """ converts a string in the first given base to the equivalent string in the second base
        arguments: B1 is the first base between 2 and 10 inclusive, B2 is the second base between 2 and 10 inclusive, s_in_B1 is the original string
    """
    num = baseBToNum(s_in_B1, B1)
    ans = numToBaseB(num, B2)
    return ans

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'

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


#function 4 add(S, T)
def add(S, T):
    """ returns the sum of S and T in binary
        arguments: S and T are two strings of binary
    """
    num1 = binaryToNum(S)
    num2 = binaryToNum(T)
    sum = num1 + num2
    ans = numToBinary(sum)
    return ans

#5 addB(S,T)
def addB(S,T):
    """ returns the sum of S and T in binary
        arguments: S and T are strings of binary numbers
    """
    if len(S) == 0 and len(T) == 0:
        return ""
    elif len(S) == 0 and len(T) != 0:
        return T
    elif len(T) == 0 and len(S) != 0:
        return S
    #recursive cases
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'
    if S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    if S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    if S[-1] == '1' and T[-1] == '1':
        return addB(addB(S[:-1], '1'), T[:-1]) + '0'
    
assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'

#helper functions
def frontNum(S):
    """returns number of times the first element of the input S appears consecutively at the start of S
    """
    if len(S) <= 1:
        return 0
    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 0
   
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


#function6 compress(S)
def compress(S):
    """ returns antoher binary string, run length encoding of the original
        argument: binary string S which has length less or equal to 64
    """
    if len(S) == 0:
        return ""
    elif S[0] == "0":
        compressAmount = frontNum(S)+1   #frontNum(S)+1 gives the index of the compressed parts
        return '0' + "0"*(7-len(numToBinary(compressAmount))) + numToBinary(compressAmount) + compress(S[compressAmount:])
    else:
        compressAmount = frontNum(S)+1
        return "1" + "0"*(7-len(numToBinary(compressAmount))) + numToBinary(compressAmount) + compress(S[compressAmount:])
    

def uncompress(C):
    """ inverts the compression in compress
        returns string S
        argument: string C
    """
    if len(C) == 0:
        return ""
    elif C[0] == "0":
        return "0"*binaryToNum(C[1:8]) + uncompress(C[8:])
    else:
        return "1"*binaryToNum(C[1:8]) + uncompress(C[8:])

assert uncompress(compress(64*'0')) == 64*'0'
assert uncompress(compress('11111')) == '11111'
assert uncompress(compress('101010')) == '101010'


    
    
