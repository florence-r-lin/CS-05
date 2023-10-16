#hw1pr1.pyCS5, hw1pr1
# Filename: hw1pr1.py
# Name: Florence Lin
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print("answer0:", answer0)

#problem 1: creating [7,1]
answer1 = e[1:3]
print("answer 1", answer1)

#problem 2: creating [9, 1, 1]
answer2 = pi[5:6] + e[2:3] + e[2:3]
print("answer 2", answer2)

#problem 3: creating [1,4,1,5,9]
answer3 = pi[1:6]
print("answer 3", answer3)

#problem 4: creating [1,2,3,4,5]
answer4 = pi[1:2] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print("answer 4", answer4)


# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]    
print("answer5:", answer5)

# Problem 6:  'collude'
answer6 = c[0:4] + m[1:3] + c[6]
print("answer6:", answer6)


# Problem 7:  'arveyudd'
answer7 = h[1:6] + m[1:4]
print("answer7:", answer7)

# Problem 8:  'hardeharharhar'
answer8 = h[0:3] + m[3] + c[4] + 3*h[0:3] 
print("answer7:", answer8)

# Problem 9:  'legomyego'
answer9 = c[3:6] + c[1] + m[0] + h[5] + h[4] + c[5] + c[1]
print("answer9:", answer9)

# Problem 10: 'clearcall'
answer10 = c[0] + c[3:5] + h[1:3] + c[0] + h[1] + c[2:4]
print("answer 10:", answer10)