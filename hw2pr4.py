# CS5 Gold: HW 2, Problem 4
# Filename: hw2pr4.py
# Name: Florence Lin
# Problem description: The four fours challenge!
# Aknowledgments: I worked individually.

def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  if weekday == True and vacation == False:
    return False
  if weekday == False and vacation == True:
    return True
  if weekday == True and vacation == True:
    return True

def monkey_trouble(a_smile, b_smile):
  if a_smile == False and b_smile == False:
    return True
  if a_smile == True and b_smile == False:
    return False
  if a_smile == False and b_smile == True:
    return False
  if a_smile == True and b_smile == True:
    return True

def sum_double(a, b):
  if a == b:
    return a*4
  else:
    return a+b

def diff21(n):
  if n > 21:
    return (n-21)*2
  else:
    return 21-n

def parrot_trouble(talking, hour):
  if talking == True and hour<7:
    return True
  elif talking == True and hour>20:
    return True
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10 or a+b==10:
    return True
  else:
    return False

def near_hundred(n):
  if abs(n-100) <=10:
    return True
  elif abs(n-200) <=10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative == True and a<0 and b<0:
    return True
  elif negative == False and a>0 and b<0:
    return True
  elif negative == False and a<0 and b>0:
    return True
  else:
    return False

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    ans = "not "+ str
    return ans

def missing_char(str, n):
  return str[0:n] + str[n+1:]

def front_back(str):
  if len(str) == 1:
    return str
  else:
   last = str[-1:]
   first = str[0:1]
   return last + str[1:-1] + first

def front3(str):
  ans = str[0:3]
  return 3*ans

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a+b+b+a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
  return out[0:2] + word + out [-2:]

def extra_end(str):
  return 3*str[-2:]

def first_two(str):
  if len(str) == 0:
    return ""
  elif len(str) < 2:
    return str
  else:
    return str[0:2]


def first_half(str):
  length = len(str)
  half = length//2
  return str[0:half]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  if len(b) < len(a):
    return b+a+b

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[0:2]

def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False

def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  else:
    return False

def sum3(nums):
  return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]
  
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]
  if nums[2] > nums[0]:
    return [nums[2], nums[2], nums[2]]
  if nums[0] == nums[2]:
    return [nums[2], nums[2], nums[2]]

def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) <= 1:
    return nums[0]
  if len(nums) == 2:
    return nums[0] + nums[1]
  if len(nums) > 2:
    return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
  if nums[1] == 2 or nums[1] == 3:
    return True
  else:
    return False

def cigar_party(cigars, is_weekend):
  if is_weekend == True and cigars >= 40:
    return True
  elif is_weekend == False and cigars>=40 and cigars<=60:
    return True
  else:
    return False

def date_fashion(you, date):
  if you<= 2 or date <=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  if is_summer == False and temp >= 60 and temp <= 90:
    return True
  elif is_summer == True and temp >= 60 and temp <= 100:
    return True
  else:
    return False

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed<= 65:
      return 0
    elif speed>65 and speed<=85:
      return 1
    else:
      return 2
  if is_birthday == False:
    if speed<= 60:
      return 0
    elif speed>60 and speed<=80:
      return 1
    else:
      return 2

def sorta_sum(a, b):
  if a+b >= 10 and a+b <= 19:
    return 20
  else:
    return a+b

def alarm_clock(day, vacation):
  if vacation == False and day!=0 and day!=6:
    return "7:00"
  if vacation == True and day==0:
    return "off"
  if vacation == True and day==6:
    return "off"
  if vacation == False and day==0:
    return "10:00"
  if vacation == False and day==6:
    return "10:00"
  if vacation == True and day!=0 and day!=6:
    return "10:00"

def love6(a, b):
  if a==6 or b==6:
    return True
  elif a-b==6 or b-a==6 or a+b==6:
    return True
  else:
    return False

def in1to10(n, outside_mode):
  if outside_mode == False and n>10:
    return False
  if outside_mode == False and n==10:
    return True
  if outside_mode == False and n>=1 and n<=10:
    return True
  if outside_mode == True and n<=1 or n>=10:
    return True
  else:
    return False

def near_ten(num):
  if num%10 <= 2 or num%10 >= 8:
    return True
  else:
    return False

def lone_sum(a, b, c):
  if a==b==c:
    return 0
  if a==c:
    return b
  if a==b:
    return c
  if b==c:
    return a
  else:
    return a+b+c