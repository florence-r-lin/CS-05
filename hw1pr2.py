# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Florence Lin
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Returns value: reutrns square of its argument
        Argument x: a number (int or float)
    """
    return x**2

def interp(low, hi, fraction):
    """returns: accepts input arguments low, hi, fraction and returns flloating point value that is fraction of the way between low and hi
        Argument low: start point
        argument hi: end point
        fraction: fraction traversed so far
    """
    return (hi-low)*fraction + low

def checkends(s):
    """returns: boolean, true if first character in string is the same as last character in string, returns false if otherwise"""   
    a = s[0]
    b = s[-1]
    return(bool(a == b))

def has42(d):
    """returns True if key 42 is in the dictionary 'd' and returns False if otherwise."""
    if 42 in d:
        return True
    else:
        return False

def hasKey(k,d):
    """reutrns true if key k is in dictionary an false otherwise"""
    if k in d:
        return True
    else:
        return False
    
def flipside(s):
    """returns first half of string s as the second half and second half of string s as first half"""
    length = len(s)//2
    ans = s[length: len(s)] + s[0: length] 
    return ans

def convertFromSeconds(s):
    """takes s(non negative seconds) and returns a list of four nonnegative integers that represents that number of seconds in more convetional units of time"""
    day = s//86400 
    s = s%86400
    hour = s//3600 
    s = s%3600
    m = s//60 
    sec = s%60
    L = [day, hour, m, sec]
    return L