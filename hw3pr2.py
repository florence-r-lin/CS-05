#
# hw3pr2.py - algorithms and use-it-or-lose-it
# Florence Lin
# collaborators: Angelina Tsai, Katherine Zhao, and Ayushi Kashyap

print("Onward, Algorithms!")

# The NEXT_CHAR dictionary for use in rotc(c)
#
NEXT_CHAR = { "a": "b", "A": "B",
              "b": "c", "B": "C",
              "c": "d", "C": "D",
              "d": "e", "D": "E",
              "e": "f", "E": "F",
              "f": "g", "F": "G",
              "g": "h", "G": "H",
              "h": "i", "H": "I",
              "i": "j", "I": "J",
              "j": "k", "J": "K",
              "k": "l", "K": "L",
              "l": "m", "L": "M",
              "m": "n", "M": "N",
              "n": "o", "N": "O",
              "o": "p", "O": "P",
              "p": "q", "P": "Q",
              "q": "r", "Q": "R",
              "r": "s", "R": "S",
              "s": "t", "S": "T",
              "t": "u", "T": "U",
              "u": "v", "U": "V",
              "v": "w", "V": "W",
              "w": "x", "W": "X",
              "x": "y", "X": "Y",
              "y": "z", "Y": "Z",
              "z": "a", "Z": "A",
}

def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    
def shiftN(c, N):
        """ returns c, shifted by N spots """
        if N == 0: return c
        return shiftN( shift1(c), N-1 )

def list_to_str(L):
    """L must be a list of characters;
       this function returns a single string made from them.
    """
    if len(L) == 0:
        return ''
    return L[0] + list_to_str(L[1:])


# function 1 encipher
def encipher(s, N):
    """returns a new string where letters in s have been rotated by N characters forward in the alphabet
       Arguments: s is a string and N is a non negative integer between 0 and 25
    """ 
    if s == "":
         return s
    else:
        return list_to_str([shiftN(x, N) for x in s])
print("encipher('xyza', 1) == 'yzab'", encipher('xyza', 1))
print("encipher('Z A', 1) == 'A B'", encipher('Z A', 1))

assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'

# table of probabilities for each letter...
def letProb(c):
    """If c is the space character or an alphabetic character,
       we return its monogram probability (for english),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
       Note: this should really be converted into a dictionary!
    """
    if c == ' ': return 0.1904
    elif c == 'e' or c == 'E':
        return 0.1017
    elif c == 't' or c == 'T':
        return 0.0737
    elif c == 'a' or c == 'A':
        return 0.0661
    elif c == 'o' or c == 'O':
        return 0.0610
    elif c == 'i' or c == 'I':
        return 0.0562
    elif c == 'n' or c == 'N':
        return 0.0557
    elif c == 'h' or c == 'H':
        return 0.0542
    elif c == 's' or c == 'S':
        return 0.0508
    elif c == 'r' or c == 'R':
        return 0.0458
    elif c == 'd' or c == 'D':
        return 0.0369
    elif c == 'l' or c == 'L':
        return 0.0325
    elif c == 'u' or c == 'U':
        return 0.0228
    elif c == 'm' or c == 'M':
        return 0.0205
    elif c == 'c' or c == 'C':
        return 0.0192
    elif c == 'w' or c == 'W':
        return 0.0190
    elif c == 'f' or c == 'F':
        return 0.0175
    elif c == 'y' or c == 'Y':
        return 0.0165
    elif c == 'g' or c == 'G':
        return 0.0161
    elif c == 'p' or c == 'P':
        return 0.0131
    elif c == 'b' or c == 'B':
        return 0.0115
    elif c == 'v' or c == 'V':
        return 0.0088
    elif c == 'k' or c == 'K':
        return 0.0066
    elif c == 'x' or c == 'X':
        return 0.0014
    elif c == 'j' or c == 'J':
        return 0.0008
    elif c == 'q' or c == 'Q':
        return 0.0008
    elif c == 'z' or c == 'Z':
        return 0.0005
    else:
        return 1.0

def letterScore(let):
    """returns the value of the character, established as a single character string, as a Scrabble tile. If the argument is not a letter, letterScore(let) returns 0
        Argument: let single character string
    """
    if let in 'AEILNORSTUaeilnorstu':
        return 1
    if let in 'dgDG':
        return 2
    if let in 'bcmpBCMP':
        return 3
    if let in 'fhvwyFHVWY':
        return 4
    if let in 'kK':
        return 5
    if let in 'jxJX':
        return 8
    if let in 'qzQZ':
        return 10
    else:
        return 0

def scrabbleScore(S):
    """takes S and returns the scrabble score of that string. non letters give 0 points. 
       Argument: S is a string argument which can have any characters
    """
    if len(S) == 0:
        return 0
    else:
        ans = letterScore(S[0]) + scrabbleScore(S[1:])
        return ans        
        
# function 2 decipher(s)
# run scrabble score for each encipher, lowest scrabble score = most common, return the string that creates the lowest scrabble score which is most likely a word
def decipher(s):
    """given a string of english text shifted by some amount, decipher will return the original enlgish string
       argument: s is a string
    """
    LC = [encipher(s, n) for n in range(26)]
    LoL = [[scrabbleScore(x),x]  for x in LC]
    minScrabble = min(LoL) 
    return minScrabble[1]

def count(e, L):
    LC = [e for x in L if x == e]
    return LC

#function 3 blsort(L)
def blsort(L):
    """ accepts list L and returns a list with the same elemtns as L but in ascending order
       handles lists of binary digits
       arugments: accepts List L which contains elements that can be represented by binary digits
    """
    return count(0,L) + count(1,L)

def remAll(e,L):
    """Returns a new copy of L with all e's removed."""
    if len(L) == 0: 
        return L
    elif L[0] == e:
        return remAll(e, L[1:])
    else:
        return L[0:1] + remAll(e, L[1:])

def remOne(e,L):
    """Returns a new copy of L with the first e removed."""
    if len(L) == 0: 
        return L
    elif L[0] == e:
        return L[1:]
    else:
        return L[0:1] + remOne(e, L[1:])

#function 4 gensort(L)
# take min of list and remove, keep adding removed to another list
def gensort(L):
    """ accepts list L and returns a list with same elements in L, but ascending order
        arguments: accepts list L
    """
    if len(L) == 0:
        return L
    if len(L) == 1:
        return L
    else:
        minimum = min(L)
        return [minimum] + gensort(remOne(minimum, L))


#function 5 jscore(S, T)
def jscore(S,T):
    """ accepts string S and T and returnst he jotto score of S compared to T
        jotto score is the number in S that is same as T
        arguments: accepts string S and string T
    """
    score = 0
    if len(S) == 0  or len(T) == 0:
        return 0
    if S[0] in T:
        return score + 1 + jscore(S[1:], remOne(T.index(S[0]), T))
    else:
        return jscore(S[1:], T)
     
#function 6, exact_change(target_amount, L)
def exact_change(target_amount, L):
    """ returns true or false based on if it possible to create target_amount by adding up some or all of L
        arguments: target_amount is one non negative int, L is list of positive nums, 
    """
    if target_amount == 0:
        return True
    elif target_amount < 0:
        return False
    elif target_amount == sum(L):
        return True
    elif len(L) == 0:
        return False
    else:
        useit = exact_change(target_amount-L[0], L[1:])
        loseit = exact_change(target_amount, L[1:])
        return useit or loseit



#function 7
def LCS(S, T):
    """ returns the longest common subsequence that S and T share. letters must appear in same order but does not have to be consecutively
        arguments: S and T are strings
    """
    if len(S) == 0 or len(T) == 0:
        return ""
    if S[0] == T[0]:
        return S[0] + LCS(S[1:], T[1:])
    else:
        result1 = LCS(S[1:], T)
        result2 = LCS(S, T[1:])
        if len(result1) > len(result2):
            return result1
        else:
            return result2


    
    
    
        
    