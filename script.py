# import sys
# print(sys.platform)
# print(2 ** 100)
# print('spam!'*8)
##############################################################################
######################## Numbers ###############################################
# print(2 ** 100)
# x  = "hello, world"
# count = 0
# for n in x:
#     if n != "":
#         count += 1
# print(count)
#     # else:
#     #     continue 
# print('\3'*6 + ' ' + x +' '+ '\3'*6)    
# print(123 + 222)
#################################################################################
# import math
# print(math.pi)
# print(math.sqrt(85))
# #################################################################################
# import random
# print(random.random())
# print(random.choice([1, 2, 3, 4]))

# for i in range(999999999):
#     print(i)

######################################### Strings ################################


# s = 'Spam'
# print(len(s)) # Length
# print(s[1]) # The first item in S, indexing by zero-based position
# print(s[1]) # The second item from the left

# print(s[-1]) # The last item from the end in S
# print(s[-2]) # The second to last item from the end

# print(s[-1])  # The last item in s
# print(s[len(s)-1])  # Negative indexing, the hard way

# print(s)  # A 4-character string
# print(s[1:3])  # Slice of S from offsets 1 through 2 (not 3)

# print(s[1:])  # Everything past the first (1:len(S))
# print(s)   # S itself hasn't changed

# print(s[0:3])    # Everything but the last
# print(s[:3])    # Same as S[0:3]

# print(s[:-1])   # Everything but the last again, but simpler (0:-1)
# print(s[:])     # All of S as a top-level copy (0:len(S))
#####################################################################################################
##################### Immutability
# s = 'z' + s[1:]
# print(s)
#####################################################################################################
# print(s.find('pa'))     # Find the offset of a substring
# print(s)
#####################################################################################################
# s = s.replace('pa', 'XYZ') # Replace occurrences of a substring with another
# print(s)

#####################################################################################################
# line = 'aaa,bbb,ccc,ddd'
# print(line.split(','))  # Split on a delimiter into a list of substrings

# s = 'spam'
# print(s.upper())    # Upper- and lowercase conversions

# print(s.isalpha())  # Content tests: isalpha, isdigit, etc.
#####################################################################################################
# line = 'aaa,bbb,cccc,ddd\n'
# line = line.rstrip()    # Remove whitespace characters on the right side
# print(line)

# print('%s, eggs, and %s ' %('spam', 'SPAM!'))   # Formatting expression (all)
# print('{0}, eggs, and {1} '.format('spam', 'SPAM!'))    # Formatting method (2.6, 3.0)

# help(s.center)

# print(s.center(50, '\3'))
# help(s.encode)
# print(s.encode(encoding='utf-8', errors='strict'))
######################################################################################################
# x = 'A\nB\tC'   # \n is end-of-line, \t is tab
# print(len(x))  # Each stands for just one character

# ord('\n')       # \n is a byte with the binary value 10 in ASCII
# print('A\oB\oC')        # \0, a binary zero byte, does not terminate string
######################################################################################################
# msg = """aaaaaaaaaaaaaaaaaaaaaaaa
# bbb'''bbbbbbbbbbbbbbb""bbbbbb'bbb
# cccccccccccccccc"""
# print(msg)
######################################################################################################
#################Pattern Matching#################
# x = 'Pattern Matching'
# print(x.center(50,'#'))

# import re 
# match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
# print(match.group(1))

# print(x.center(50,'#'))
# match = re.match('/(.*)/(.*)/(.*)', '/usr/@home/lumberjack')
# print(match.groups())
#######################################################################################################
#####################################Lists######################################
# print('Lists'.center(80,'#'))   # A list of three different-type objects
# l = [123, 'spam', 1.23]     # Number of items in the list
# print(len(l))
# print(l[0])
# print(l[:-1])       # Slicing a list returns a new list
# print(l + [4, 5, 6])    # Concatenation makes a new list too
# ###########################Type-Specific Operationss############################
# print('Type-Specific Operationss'.center(80, '#'))
# l.append('NI')      # Growing: add object at end of list
# print(l)
# l.pop(2)    # Shrinking: delete an item in the middle
# # print(l)        # "del L[2]" deletes from a list too
# M = ['bb', 'aa', 'cc']

# # M.remove('bb') # remove a given item by value
# M.sort()
# # M.insert(0, 20)     #insert an item at an arbitrary position
# print(M)

# M.reverse()
# print(M)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥Bounds Checking♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ 
# print('Bounds Checking'.center(80, '\3'))
# print(M[99])
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Nesting☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# print('Nesting'.center(80, '\2'))

# M = [[1,2,3],[4,5,6],[7,8,9]]
# print(M)
# print(M[1])
# print(M[1][2])

# print('Comprehensions'.center(80, '\2'))

# col2 = [row[1] for row in M]    # Collect the items in column 2
# print(col2)

# print([row[1] * 2 for row in M])
# print([row[1] + 1 for row in M])        # Add 1 to each item in column 2

# print([row[1] for row in M if row[1] % 2 == 0])     # Filter out odd items
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥Collect a diagonal from matrix♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# print('Collect a diagonal from matrix'.center(80, '\3'))
# diag = [M[i][i] for i in [0, 1, 2]]
# print(diag)
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥Repeat characters in a string♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# print('Repeat characters in a string'.center(80, '\3'))
# doubles = [c * 2 for c in 'abdo']
# print(doubles)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ Create a generator of row sums ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# G = (sum(row) for row in M)
# print(next(G))      # Run the iteration protocol
# print(next(G))      # Run the iteration protocol
# print(next(G))      # Run the iteration protocol
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ # Map sum over items in M ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# a = list(map(sum, M))
# print(a)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ # Create a set of row sums ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# c = {sum(row) for row in M}
# print(c)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ # Creates key/value table of row sum ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# d = {i : sum(M[i]) for i in range(3)}
# print(d)
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ # List of character ordinals ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# l = [ord(x) for x in 'spaam']
# print(l)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ # Sets remove duplicates ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# li = {ord(x) for x in 'spaam'}
# print(li)
# #♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥  Dictionary keys are unique ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# lis = {x: ord(x) for x in 'spaam'}
# print(lis)
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Dictionaries♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  
# print('Dictionaries'.center(80, '\4'))
# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Mapping Operations♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦ 
# D = {'food': 'spam', 'quantity': 4, 'color': 'pink'} 
# print(D['food'])        # Fetch value of key 'food'
# D['quantity'] += 1      # Add 1 to 'quantity' value
# print(D)
##♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦# Create keys by assignment♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
# D = {}
# D['name'] = 'Bob'
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
# print(D['name'])
#♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Nesting Revisited♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  
# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
#        'job': ['dev', 'mgr'],
#        'age': 40.5}

# print(rec['name'])      # 'name' is a nested dictionary
# print(rec['name']['last'])      # Index the nested dictionary
# print(rec['job'])       # 'job' is a nested list
# print(rec['job'][-1])   # Index the nested list
# rec['job'].append('programmer')     # Expand Bob's job description in-place
# print(rec['job'])
#♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦Sorting Keys: for Loops♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  
# D = {'a': 1, 'b': 2, 'c': 3}
# print(D)

# Ks = list(D.keys())     # Unordered keys list
# print(Ks)

# Ks.sort()       # Sorted keys list
# print(Ks)

# for key in Ks:                  # Iterate though sorted keys
#     print(key, '==>', D[key])   # <== press Enter twice here
    
# for key in sorted(D):
#     print(key, '==>', D[key])
    
# for c in 'spam':
#     print(c.upper())
    
# x = 10
# while x > 0:
#     print('\1\3' * x)
#     x -= 1

# while x < 10:
#     print('\3\1' * x)
#     x += 1   
# ♥☺
# ♥☺♥☺
# ♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ 
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥
# ☺♥☺♥
# ☺♥
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Iteration and Optimization☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# print('Iteration and Optimization'.center(80, '\2'))
# squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
# print(squares)

# squares = []
# for x in [1, 2, 3, 4, 5]:  # This is what a list comprehension does
#     squares.append(x ** 2) # Both run the iteration protocol internally
# print(squares)
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Missing Keys: if Tests☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# D['e'] = 99
# print(D)
# # print(D['f'])

# # print('f' in D)
# if not 'f' in D:
#     print('missing')

# value = D.get('x', 0)                # Index but with a default
# print(value)

# value = D['x'] if 'x' in D else 0       # if/else expression form
# print(value)
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Tuples☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# T = (1, 2, 3, 4)    # A 4-item tuple
# print(len(T))       # Length

# T1 = T + (5, 6)     # Concatenation
# # print(T1)

# print(T1[0])

# print(T.index(4))   # Tuple methods: 4 appears at offset 3

# print(T.count(4))   # 4 appears once

# T[0] = 2        # Tuples are immutable
# print(T)

# t = ('spam', 3.0, [11, 22, 33])
# print(t[1])
# print(t[2][1])

# t.append(4)     #AttributeError: 'tuple' object has no attribute 'append'
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Files☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# f = open('data.txt', 'w')   # Make a new file in output mode
# f.write('Hello\n')      # Write strings of bytes to it
# f.write("world!\n")     # Returns number of bytes written in Python 3.0
# f.close()               # Close to flush output buffers to disk        


# f = open('data.txt')        # 'r' is the default processing mode
# text = f.read()             # Read entire file into a string

# print(text)                 # print interprets control characters
# print(text.split())         # File content is always a string
# help(f.seek)

# data = open('data.bin', 'rb').read()        # Open binary file
# print(data)                                 # bytes string holds binary data
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻Other Core Types☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
# x=set('spam')       # Make a set out of a sequence in 2.6 and 3.0
# y = {'h', 'a', 'm'} # Make a set with new 3.0 set literals
# print(x, y)
# print(x & y)        # Intersection
# print(x | y)        # Union
# print(x - y)        # Difference

# z = {x ** 2 for x in [1, 2, 3, 4]}      # Set comprehensions
# print(z)
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥# Floating-point (use .0 in Python 2.6)♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#print('# Floating-point (use .0 in Python 2.6)'.center(80, '\3'))
# # print(1/3)
# # print(2/3 + 1/2)
# import decimal                  # Decimals: fixed precision
# d = decimal.Decimal('3.141')
# print(d + 1)
# decimal.getcontext().prec = 2
# print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))
# from fractions import Fraction      # Fractions: numerator+denominator
# f = Fraction(2, 3)
# print(f + 1)

# print(f + Fraction(1, 2))
# print('# Floating-point (use .0 in Python 2.6)'.center(80, '\3'))
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥# # Booleans♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# print(1 < 2, 1> 2)
# print(bool('spam'))

# x = None
# print(x)

# l = [None] * 100
# print(l)
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥# # How to Break Your Code’s Flexibility♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# print(type(D))
# print(type(type(D)))
# l = [1, 2, 3, 5, 6]
# if type(l) == type([1, 5]):     # Type testing, if you must.
#     print('yes')
    
# if type(l)== list:                 # Using the type name
#     print('yes')
    
# if isinstance(l, list):             # Object-oriented tests
#     print('yes')

# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺  User-Defined Classes ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# class Worker:
#     def __init__(self, name, pay):  # Initialize when created
#         self.name = name            # self is the new object
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]    # Split string on blanks
#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent)     # Update pay in-place
            
# bob = Worker('bob smith', 50000)    # Make two instances
# sue = Worker('Sue Jones', 60000)    # Each has name and pay attrs
# print(bob.lastName())               
# bob.giveRaise(10)                   # Call method: bob is self
# print(bob.pay)
# print(bob.name)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺  Numeric Literals     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺

# Literal                              Interpretation
# 1234, −24, 0, 99999999999999         Integers (unlimited size)
# 1.23, 1., 3.14e-10, 4E210, 4.0e+210  Floating-point numbers
# 0177, 0x9ff, 0b101010                Octal, hex, and binary literals in 2.6
# 0o177, 0x9ff, 0b101010               Octal, hex, and binary literals in 3.0
# 3+4j, 3.0+4.0j, 3J                   Complex number literals
# a = -123
# print(pow(a, 2))
# print(abs(a))
# print(round(a))
# print(int(a))
# print(hex(a))
# print(bin(a))

# print(int(3.1415))  # Truncates float to integer
# print(float(3))     # Converts integer to float

# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                              ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺  Numeric Display Formats     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                             ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# b = 2
# a = 3
# # print(b/(2.0 + a))
# num = 1 / 3.0
# # print(num)
# print('%e' %num)                # String formatting expression

# print('%4.2f' %num)             # Alternative floating-point format

# print('{0:4.3f}'.format(num))   # String formatting method (Python 2.6 and 3.0)

# print(repr(num))        # Used by echoes: as-code form
# print(str(num))         # Used by print: user-friendly form

# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                      ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺  Comparisons: Normal and Chained     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                      ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# 1 < 2 # Less than
# True
# 2.0 >= 1 # Greater than or equal: mixed-type 1 converted to 1.0
# True
# 2.0 == 2.0 # Equal value
# True
# 2.0 != 2.0 # Not equal value
# False

# x = 2
# y = 4 
# z = 6
# print(x // y)
# print(z//y)

################### Floor versus truncation
# import math
# print(math.floor(2.5))
# print(math.floor(-2.5))
# print(math.trunc(2.5))
# print(math.trunc(-2.5))
# ♥                                       ♥
# ♥☺                                     ♥☺
# ♥☺♥☺                                 ♥☺♥☺
# ♥☺♥☺♥☺                             ♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺                         ♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺                     ♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺                 ♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺             ♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺         ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥☺♥
# ☺♥☺♥☺♥
# ☺♥☺♥
# ☺♥
# ♥        Complex Numbers
# c = 5 + 1j

# print(c * 1j)
## Hexadecimal, Octal, and Binary Notation

# a, b , c  = 0o1, 0o20, 0o377          # Octal literals
# print(a, b , c)

# a, b, c = 0x1, 0x10, 0xFF             # Hex literals
# print(a, b , c)     

# a, b, c = 0b1, 0b10000, 0b11111111     # Binary literals
# print(a, b, c)

# b = oct(64), hex(64), bin(64)
# print(b)

# print(int(64), int('100', 8), int('40', 16), int('01000000', 2))
# print(int('0x40', 16), int('0b1000000', 2))        # Literals okay too
# print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
############# string formatting
# print('{2:o}, {1:x}, {0:b}'.format(64, 64, 64))
# print('%o, %x, %X' %(64, 255, 255))

# X = 0xFFFFFFFFFFFFFFFFFFFFFFFF
# print(X)
# print(oct(X))
# print(bin(X))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   Bitwise Operations  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# x = 1             # 0010
# print(x << 2)       # Shift left 2 bits: 0100
# print(x | 2)        # Bitwise OR: 0011
# print(x & 1)        # Bitwise AND: 0001

# X = 0b0001 # Binary literals
# X << 2 # Shift left
# 4
# bin(X << 2) # Binary digits string
# '0b100'
# bin(X | 0b010) # Bitwise OR
# '0b11'
# bin(X & 0b1) # Bitwise AND
# '0b1'
# X = 0xFF # Hex literals
# bin(X)
# '0b11111111'
# X ^ 0b10101010 # Bitwise XOR
# 85
# bin(X ^ 0b10101010)
# '0b1010101'
# int('1010101', 2) # String to int per base
# 85
# hex(85) # Hex digit string
# '0x55'

# x = 99
# print(bin(x), x.bit_length())
# print(bin(256), (256).bit_length())
# print(len(bin(256)) - 2)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   Other Built-in Numeric Tools  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# import math
# print(math.pi, math.e)        # Common constants

# print(math.sin(2 * math.pi / 180))        # Sine, tangent, cosine

# print(math.sqrt(144), math.sqrt(2))       # Square root
# print(pow(2, 4), 2 ** 4)                  # Exponentiation (power)
# print(abs(-42.0), sum((1, 2, 3, 4, 54)))  # Absolute value, summation
# print(min(25, 45, 78, 31), max(3, 1, 2, 4))   # Minimum, maximum

# math.floor(2.567), math.floor(-2.567)   # Floor (next-lower integer)
# math.trunc(2.564), math.trunc(-2.456)   # Truncate (drop decimal digits)
# int(2.456), int(-2.123)                 # Truncate (integer conversion)
# round(2.147), round(2.478), round(2.587, 2) # Round (Python 3.0 version)
# print('%1f' %2.567, '{0:.2f}'.format(2.567))    # Round for display (Chapter 7)

# print((1/3), round(1/3, 2), ('%.2f' %(1/3)))
# import math
# math.sqrt(144) # Module
# 12.0
# 144 ** .5 # Expression
# 12.0
# pow(144, .5) # Built-in
# 12.0
# math.sqrt(1234567890) # Larger numbers
# 35136.418286444619
# 1234567890 ** .5
# 35136.418286444619
# pow(1234567890, .5)
# 35136.418286444619
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   random  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# import random
# print(random.random())
# print(random.random())

# print(random.randint(1, 100))

# y = random.choice(['a', "c", 'b', 'f', "d", 'n', 2, 5, 8])
# print(y)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺    Decimal Type       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# from decimal import Decimal as de 
# print(de('0.1') + de('0.1'))
# import decimal
# # print(de(1) / de(7))
# decimal.getcontext().prec = 4
# print(de(1) / de (7))
# print(de(1))
# # print(1999 + 1.33)
# # pay = de(str(1999 + 1.33))
# # print(pay)

# # print(de('1.00') / de('3.00'))

# with decimal.localcontext() as ctx:
#     ctx.prec = 2
#     print(de('1.00') / de('3.00'))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺    Fraction Type     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# from fractions import Fraction
# print(Fraction(1.46548841346854))
# print((2.5).as_integer_ratio())     # float object method

# f = 2.5
# z = Fraction(*f.as_integer_ratio())     # Convert float -> fraction: two args
# print(z)                                # Same as Fraction(5, 2)
# x = Fraction(1, 3)

# print(x + z)

# print(float(x))
# print(Fraction.from_float(1.75))
# print(Fraction.from_decimal(23))
# print(Fraction(*(1.75).as_integer_ratio()))

#  x
# Fraction(1, 3)
#  x + 2 # Fraction + int -> Fraction
# Fraction(7, 3)
#  x + 2.0 # Fraction + float -> float
# 2.3333333333333335
#  x + (1./3) # Fraction + float -> float
# 0.66666666666666663
#  x + (4./3)
# 1.6666666666666665
#  x + Fraction(4, 3) # Fraction + Fraction -> Fraction
# Fraction(5, 3)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺        Sets          ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# x = set('abcde')
# y = set('bdxyz')
# print(x)
# print(y)
# print('e' in x)     # Membership
# print(x - y)        # Difference
# print(x | y )       # Union
# print(x & y)        # Intersection
# print(x ^ y)        # Symmetric difference (XOR)

# z = x.intersection(y)
# # print(z)
# z.add('spam')
# # print(z)
# z.update({'g', 'r'})
# # print(z)
# # z.remove('b')
# # print(z)
# for item in z:
#     print(item*3)

# S = set([1, 2, 3])  
# # print(S | set([3, 4]))      # Expressions require both to be sets
# # print(S.union([3, 4]))
# # print(S.intersection((1, 2, 5)))
# # print(S.issubset(range(-5, 5)))
# print('|'* 50)

# s = {x ** 2 for x in {1, 5, 9, 7, 3}}
# print(s)

# s1 = {x for x in 'spam'}
# print(s1)
# s2 = {c * 4 for c in 'spam'}
# print(s2)
# L = [1, 2, 3, 4, 5]
# print(set(L))
# print(list(set(L)))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺      Booleans          ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥
# print(type(True))
# print(isinstance(True, int))
# print(True == 1)
# print(True is 1)
# print(True or False)
# print(True + 4)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                  ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺  String Literals    ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                  ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# print("s\tp\na\0m")     #Escape sequences
# print(r"D:\Abdo Legrou\Python Pdf\test.spm")        #Raw strings
# print("hello\'world")
# print("hello\"world")
# print("hello\\world")
# print("hello\a world")
# print("hello\b world")
# print("hello\fworld")
# print("hello\rworld")
# print("hello\tworld")
# print("hello\vworld")
# print("hello\oooworld")
# print("hello\0world")
# s  = 'a\x00b\x00c'
# print(len(s))

#############Raw Strings Suppress Escapes
# myfile = open(r'D:\Abdo Legrou\Nouveau dossier\text.dat', 'w')
# path = r"D:\Abdo Legrou\Nouveau dossier\text.dat"
# print(path)
# print(len(path))
# mantra = """Always look
#     on the bright
#     side of life."""
# print(mantra)

# s = 'abcdefghijklmnop'
# print(s[1:10:2])
# print(s[::2])

# st = 'hello world!'
# print(st[::-1])
# s = 'abcedfg'
# print(s[5:1:-1])
# print('spam'[1:3])
# print('spam'[slice(1, 3)])
# print('spam'[::-1])
# print('spam'[slice(None, None, -1)])
# import sys
# print(sys.argv)
################### String Conversion Tools
# print("42" + 1)
# print(int("42"), str(42))
# print(repr(42))
# print(ord('s'))
# print(chr(115))
# print(int('1001', 2))
# print(bin(13))
# print(bin())
#################### Changing Strings
# S = 'Spam Is Spam, Where Spam Is Spam!'
# s = s + 'SPAM!'
# s = s[:4] + 'Burger' + s[-1]
# print(s)

# s = s.replace('Bu', 'Hu')
# print(s)

# print('That is %d %s bird!' %(1, 'dead'))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                               ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   String method calls in Python   ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                               ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.

# print(S.capitalize())
# help(S.ljust)
# print(S.ljust(100, '\2'))# S.ljust(width [, fill])
# print(S.center(100, '\3'))# S.center(width [, fill])
# print(S.lower())
# print(S.count('m', 0, length(S)))# S.count(sub [, start [, end]])
# print(S.lstrip('S'))# S.lstrip([chars])
# if S.startswith('S') == True:
#     print(S.lstrip('S'))
    
# S.encode([encoding [,errors]])

# S.maketrans(x[, y[, z]])

# S.endswith(suffix [, start [, end]]) 
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======>  print(line.endswith('Ni!'))

# S.partition(sep)

# S.expandtabs([tabsize])

# S.replace(old, new [, count])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(S.replace('Spam', 'Eggs', 2))

# S.find(sub [, start [, end]])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(S.find('Spam'))

# S.rfind(sub [,start [,end]])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(S.find('Spam'))

# S.format(fmtstr, *args, **kwargs)
 
# S.rindex(sub [, start [, end]])

# S.index(sub [, start [, end]]) 

# S.rjust(width [, fill])

# S.isalnum() 

# S.rpartition(sep)

# S.isalpha() 
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(line.isalpha())

# S.rsplit([sep[, maxsplit]])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> cols = line.split()

# S.isdecimal() 

# S.rstrip([chars])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(line.rstrip('ab')) # default value is '\n'

# S.isdigit()

# S.split([sep [,maxsplit]])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> cols = line.split()

# S.isidentifier() 

# S.splitlines([keepends])

# S.islower()

# S.startswith(prefix [, start [, end]])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(S.startswith('Spam'))

# S.isnumeric()

# S.strip([chars])
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======>  print(line.strip())

# S.isprintable()

# S.swapcase()

# S.isspace()

# S.title()

# S.istitle()

# S.translate(map)

# S.isupper()

# S.upper()
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> print(line.upper())

# S.join(iterable)
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥ ======> s = ''.join(L) L=[l, r, y, i, l]

# S.zfill(width)

# s = S[:3] + 'xx' + S[5:]
# print(s)
# s = S.replace('m', 'xx')
# print(s)
# print('aa$bb$cc$dd'.replace('$', 'SPAM'))
# S = 'My Spam Is Spam, Where Spam Is Spam!'
# print(S.find('Spam'))
# print(S.replace('Spam', 'Eggs'))
# print(S.replace('Spam', 'Eggs', 2))
# print(S)
# print(list(S))
# L = list(S)
# L[0] = 'W'
# print(L)
# s = ''.join(L)
# print(s)
# print('\3'.join(['eggs', 'sausage', 'ham', 'toast']))
# line = 'aaa bbb ccc'
# col1 = line[0:3]
# col3 = line[8:]
# print(col1)
# print(col3)
# cols = line.split() # default value is espace
# cols = S.split('m')
# print(cols)
# line = 'bob, hacker, 40'
# print(line.split(','))
# line = "i'mSPAMaSPAMlumberjack"
# print(line.split('SPAM'))

# line = " The Knights who say Ni!"
# print(line.rstrip('ab')) # default value is '\n'
# print(line.strip())
# # print(line)
# print(line.upper())
# print(line.isalpha())
# print(line.endswith('Ni!'))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   Advanced String Formatting Expressions   ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# x = 1234
# res = "integers: ...%d...%-6d...%06d" %(x,x,x)
# print(res)
# x = 1.23456789
# print('%e | %f | %g' %(x,x,x))
# print(('%e' %x))
# print('%-6.2f | %05.2f | %+06.1f' %(x,x,x))
# print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺   Dictionary-Based String Formatting Expressions   ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# print("%(n)d %(x)s" % {"n":1, "x":"spam"})
# reply = """
# Greetings...
# Hello %(name)s!
# Your age squared is %(age)s
# """
# values = {'name': 'Bob', 'age': 40}
# print(reply % values)
# food = 'spam'
# age = 40
# {'food': 'spam', 'age': 40}
# # print(vars())
# print("%(age)d %(food)s" % vars())
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺      String Formatting Method Calls      ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# template = '{0}, {1} and {2}'
# print(template.format( 'spam', 'ham', 'eggs'))
# template = '{motto}, {pork} and {food}'
# print(template.format( motto = 'spam', pork ='ham', food = 'eggs'))
# template = '{motto}, {0} and {food}'
# print(template.format(  'ham',motto = 'spam', food = 'eggs'))
# print(template.split('and'))
# X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
# print(X)
# y = X.replace('and', 'but under no circumstances')
# print(y)
# import sys
# print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
# somelist = list('SPAM')
# print(somelist)
# print('first={0[0]}, third={0[2]}'.format(somelist))
# print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
# parts = somelist[0], somelist[-1], somelist[1:3]
# print('first={0}, last={1}, middle={2}'.format(*parts))
# print('{0:10} = {1:10}'.format('spam', 123.4567))
# print('{0:>10} = {1:<10}'.format('spam', 123.4567))
# print('{0.platform:>10} = {1[item]:<10}'.format(sys, dict(item='laptop')))
# print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
# print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

# print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
# print(bin(255), int('11111111', 2), 0b11111111)
# print(hex(255), int('FF', 16), 0xFF)
# print(oct(255), int('377', 8), 0o377, 0o377)
# print('{0:.2f}'.format(1 / 3.0))
# print('%.2f' % (1 / 3.0))
# print('{0:.{1}f}'.format(1 / 3.0, 4))
# print('%.*f' % (4, 1 / 3.0))
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺      Lists and Dictionaries              ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# L = [] An empty list
# L = [0, 1, 2, 3] Four items: indexes 0..3
# L = ['abc', ['def', 'ghi']] Nested sublists
# L = list('spam')
# L = list(range(-4, 4))
# Lists of an iterable’s items, list of successive integers
# L[i]
# L[i][j]
# L[i:j]
# len(L)

# L1 + L2
# L * 3
# Concatenate, repeat
# for x in L: print(x)
# 3 in L
# Iteration, membership
# L.append(4)
# L.extend([5,6,7])
# L.insert(I, X)
# Methods: growing
# L.index(1)
# L.count(X)
# Methods: searching
# L.sort()
# L.reverse()
# Methods: sorting, reversing, etc.
# del L[k]
# del L[i:j]
# L.pop()
# L.remove(2)
# L[i:j] = []
# Methods, statement: shrinking
# L[i] = 1
# L[i:j] = [4,5,6]
# Index assignment, slice assignment
# L = [x**2 for x in range(5)]
# list(map(ord, 'spam'))
# l = ['N!'] * 5
# print(l)
# res = [c * 4 for c in 'SPAM']
# print(res)
# res = []
# for c in 'SPAM':
#     res.append(c * 3)
# print(res)

# print(list(map(abs, [-1, -2, 0, 1, 2])))
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# print(matrix[1])
# print(matrix[1][1])
# matrix[1] = ["a", "b", "c"]
# print(matrix)
# matrix[1:] = ['c', 'd', 'c'], ['g', 'k', 'r']
# print(matrix)
# matrix.append('please')
# print(matrix.sort())
# L = ['agh', 'rgfh', 'atfhh', 'vjo']
# # print(L)
# # L.sort()
# L.sort(key=str.lower)
# L.sort(key=str.lower, reverse=True)
# print(sorted(L, key=str.lower, reverse=False))
# print(sorted([x.lower() for x in L], reverse=True))
# print(L)
# L = [1, 2]
# L.extend([3, 4, 5]) # Add many items at end
# L.append([3, 4, 5])
# print(L.pop())      # Delete and return last item
# L.reverse()         # In-place reversal method   
# print(L)
# print(list(reversed(L)))    # Reversal built-in with a result
# L = []
# L.append(2)
# L.append(3)                 # Push onto stack
# print(L)
# L.pop()                     # Pop off stack
# print(L)
# L = ['spam', 'eggs', 'ham']
# # print(L.index('eggs'))          # Index of an object
# # L.insert(1, 'toast')            # Insert at position
# # L.remove('eggs')                # Delete by value
# # L.pop(1)                        # Delete by position
# # print(L)
# del L[0]                          # Delete one item
# print(L)
# del L[1:]
# print(L)
# L = ['Already', 'got', 'one']
# L[1:] = []
# print(L)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                 Dictionaries              ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# D = {} Empty dictionary
# D = {'spam': 2, 'eggs': 3} Two-item dictionary
# D = {'food': {'ham': 1, 'egg': 2}} Nesting
# D = dict(name='Bob', age=40)
# D = dict(zip(keyslist, valslist))
# D = dict.fromkeys(['a', 'b'])
# Alternative construction techniques:
# keywords, zipped pairs, key lists
# D['eggs']
# D['food']['ham']
# Indexing by key
# 'eggs' in D Membership: key present test
# D.keys()
# D.values()
# D.items()
# D.copy()
# D.get(key, default)
# D.update(D2)
# D.pop(key)
# Methods: keys,
# values,
# keys+values,
# copies,
# defaults,
# merge,
# delete, etc.
# len(D) Length: number of stored entries
# D[key] = 42 Adding/changing keys
# del D[key] Deleting entries by key
# list(D.keys())
# D1.keys() & D2.keys()
# from grapheme import length


# D = {'spam': 2, 'ham': 1, 'eggs': 3}        # Make a dictionary
# # print(D['eggs'])                            # Fetch a value by key
# # print(D)
# # print(len(D))
# # print(list(D.keys()))                       # Create a new list of my keys
# # D['ham'] = ['grill', 'bake', 'fry']
# # print(D)
# # del D['eggs']
# # D['brunch'] = 'Bacon'
# # print(D)
# # print(list(D.values()))
# # print(list(D.items()))
# # print(D.get('spam'))                        # A key that is there
# # print(D.get("toast"))                       # A key that is missing 
# # print(D.get("toast", 88))

# # D2 = {"toast": 88, 'muffin': 5}
# # D.update(D2)
# # print(D)
# # D.pop("muffin")                             # Delete and return from a key
# # print(D)
# table = {'Python': 'Guido van Rossum',
#          'Perl': 'Larry Wall',
#          'Tcl':  'John Ousterhout'}
# # for lang in table:
# #     print(lang, '\t', table[lang])
# # L = []
# # L[99] = 'spam'
# # print(L)
# D = {}
# D[99] = "spam"
# # print(D[99])
# # print(D)

# Matrix = {}
# Matrix[(2, 3, 4)] = 88
# Matrix[(7, 8, 9)] = 99
# x , y, z  = 1, 5, 6
# Matrix[(x, y, z)] = 88
# print(Matrix)

# if (2, 3, 4) in Matrix:           # Check for key before fetch
#     print(Matrix[(2, 3, 4)])      # See Chapter 12 for if/else
# else:
#     print(0)

# try:
#     print(Matrix[(2, 3, 4)])        # Try to index
# except KeyError:                    # Catch and recover
#     print(0)                        # See Chapter 33 for try/except
# print(Matrix.get((2, 3, 4), 0)) 
# print(Matrix.get((2, 3, 5), 'Not Found!'))   

# rec = {}
# rec['Name'] = 'Abdo'
# rec['Age'] = 45
# rec['Job'] = ['Programmer', 'Desiener']
# rec['Gender'] = 'man'
# print(rec['Job'][0]) 

# import anydbm
# file = anydbm.open('filename')
# file['key'] = 'data'
# data = file['key']
    
# import cgi
# form = cgi.FieldStorage()
# if 'name' in form:
#     print('Hello, ' + form['name'].value)

# print(dict(name='abdo', age=45))
# print(dict([('name', 'mel'), ('age', 45)]))
# print(dict.fromkeys(['a', 'b'], 0))

# print(list(zip([x*2 for x in 'spam'], [1, 2, 3, 4])))
    
# print(length('spam'))

# D = dict(zip([x*2 for x in 'spam'], [1, 2, 3, 4]))
# print(D)
# D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
# print(D)
# D = {x: x ** 2 for x in [1, 2, 3, 4]}
# D = {c: c * 4 for c in 'SPAM'}
# D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
# D = dict.fromkeys(['a', 'b', 'c'], 0)
# D = {k:0 for k in ['a', 'b', 'c']}
# D = dict.fromkeys('spam')
# D = {k: None for k in 'spam'}

# D = dict(a=1, b=2, c=3)
# K = D.keys()
# # print(K)
# V = D.values()
# # print(V)
# # print(D.items())
# # for k ,v in D.items():
# #     print(f'{k} \t {v}')

# # print(K | {'x': 4})
# # print(V & {'x': 4})   TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
# # print(V & {'x': 4}.values())   TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
# ########################## Sorting dictionary keys ################################
# for k in sorted(K): print(k, D[k])
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                 Tuples                    ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# () An empty tuple
# T = (0,) A one-item tuple (not an expression)
# T = (0, 'Ni', 1.2, 3) A four-item tuple
# T = 0, 'Ni', 1.2, 3 Another four-item tuple (same as prior line)
# T = ('abc', ('def', 'ghi')) Nested tuples
# T = tuple('spam') Tuple of items in an iterable
# T[i]
# T[i][j]
# T[i:j]
# len(T)
# Index, index of index, slice, length
# T1 + T2
# T * 3
# Concatenate, repeat
# for x in T: print(x)
# 'spam' in T
# [x ** 2 for x in T]
# Iteration, membership
# T.index('Ni')
# T.count('Ni')
from re import S
from tracemalloc import start
from sympy import sequence


y = (1, 2) + (3, 4)
# print(y)
# print(y * 5)
# print(y[0], y[1:3])
# t = list(c * 2 for c in 'spam')
# t.sort()
# print(t)
# T = tuple(t)

# print(T)
# print(sorted(T))

# T = (1, 2, [1, 3], 3, 4, 5, 6, 2, 3, 3)
# # L = [x + 20 for x in T]
# # print(L)
# print(T.index(3))
# T.index(3, 3)
# print(T.count(3))

# T[2][0] = 'spam'
# print(T)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺            file operations                ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# output = open(r'C:\spam', 'w') Create output file ('w' means write)
# input = open('data', 'r') Create input file ('r' means read)
# input = open('data') Same as prior line ('r' is the default)
# aString = input.read() Read entire file into a single string
# aString = input.read(N) Read up to next N characters (or bytes) into a string
# aString = input.readline() Read next line (including \n newline) into a string
# aList = input.readlines() Read entire file into list of line strings (with \n)
# output.write(aString) Write a string of characters (or bytes) into file
# output.writelines(aList) Write all line strings in a list into file
# output.close() Manual close (done for you when file is collected)
# output.flush() Flush output buffer to disk without closing
# anyFile.seek(N) Change file position to offset N for next operation
# for line in open('data'): use line File iterators read line by line
# open('f.txt', encoding='latin-1') Python 3.0 Unicode text files (str strings)
# open('f.bin', 'rb') Python 3.0 binary bytes files (bytes strings)
# myfile = open('myfile.txt', 'w')            # Open for text output: create/empty
# myfile.write('Hello text file\n')           # Write a line of text: string
# myfile.write('goodbye text file\n')
# myfile.close()                              # Flush output buffers to disk

# # myfile = open('myfile.txt')               # Open for text input: 'r' is default
# # print(myfile.readline())                  # Read the lines back
# # print(myfile.readline())
# # print(myfile.readline())
# # print(open('myfile.txt').read())
# for line in open('myfile.txt'):
#     print(line, end='')

# data = open('data.bin', 'rb').read() # Open binary file: rb=read binary
# print(data)# bytes string holds binary data
# # b'\x00\x00\x00\x07spam\x00\x08'
# print(data[4:8]) # Act like strings
# # b'spam'
# print(data[0]) # But really are small 8-bit integers
# # 115
# print(bin(data[0])) # Python 3.0 bin() function

# x, y , z = 43, 44, 45
# s = 'spam'
# d = {'a':1, 'b':2}
# l = [1, 2, 3]
# f = open('datafile.txt', 'w')
# f.write(s + '\n')
# f.write('%s, %s, %s\n' %(x, y, z))
# f.write(str(l) + '$' + str(d) + '\n')
# f.close()

# chars = open('datafile.txt').read()
# print(chars)

# f = open('datafile.txt')
# line = f.readline()
# print(line)
# print(line.rstrip())
# line = f.readline()
# print(line)
# print(line.split(','))
# print(line.rstrip().split(','))
# line = f.readline()
# print(line)
# prts = line.split('$')
# print(prts)
# D = {'a':1, 'b':2}
# F = open('datafile.pkl', 'wb')
# import pickle
# pickle.dump(D, F)
# F.close()
# # F = open('datafile.pkl', 'rb')
# # E = pickle.load(F)
# # print(E)
# print(open('datafile.pkl', 'rb').read())

# f = open('data.bin', 'wb')
# # import struct
# # data = struct.pack('>i4sh', 7, 'spam', 8)
# # f.write(data)
# # f.close()
# data = f.read()
# print(data)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺    References Versus Copies     ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# x = [1, 2, 3]
# l = ['a', x, 'b']       # Embed references to X's object
# d = {'x': x, 'y':2}

# x[1] = 'surprise'
# print(l)
# print(d)

# L = [1, 2, 3]
# D = {'a': 1, 'b':2}

# A = L[:]
# B = D.copy()
# A[1] = 'Ni'
# B['c'] = 'spam'
# print(L, D)
# print(A, B)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺    Comparisons, Equality, and Truth    ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# L1 = [1, ('a', 3)]
# L2 = [1, ('a', 3)]
# print(L1 == L2, L1 is L2)

# S1 = 'spam'
# S2 = 'spam'
# print(S1 == S2, S1 is S2)
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺           Doing Math on User Input        ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# reply = '20'
# # print(reply ** 2)      #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print(int(reply) ** 2)
# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     elif not reply.isdigit():print(' Bad! Boy' * 2)
#     else:print(int(reply) ** 2)
# print('Bye')

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop':
#         break
#     try:
#         num = int(reply)
#     except:
#         print(' Bad! Boy' * 2)
#     else:
#         print(int(reply) ** 2)
# print('Bye')

# s = '123'
# t = 'xxx'
# print(s.isdigit(), t.isdigit())

# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺    Nesting Code Three Levels Deep    ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         num = int(reply)
#         if num < 20:
#             print('low')
#         else:
#             print(num ** 2)
# print('Bye')

# for (a, b , c) in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
#     print(a, b, c)
# L = [1, 2, 3, 4]
# while L:
#     front, L = L[0], L[1:]      # See next section for 3.0 alternative
#     print(front, L)

# seq = [1, 2, 3, 4]
# # a, b, c, d = seq
# # print(a, b, c, d)
# a, *b = seq 
# # print(a)
# # print(b)
# # *a, b = seq
# # print(a)
# # print(b)
# a= '#' * 20
# L=[]
# for c in a: L.append(c)
# # print(b)
# while L:
#     # front, *L = L
#     *L , head = L
#     # print(front, L)
#     print(L, head)

# seq = [1, 2, 3, 4]
# a, b, c, *d = seq
# print(a, b, c, d)
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] #   
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] #        
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#', '#'] #
# ['#', '#', '#', '#'] #
# ['#', '#', '#'] #
# ['#', '#'] #
# ['#'] #
# [] #

# for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
#     print(a, b, c)

# for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
#     a, b, c = all[0], all[1:3], all[3]
#     print(a, b ,c)

# a = b = c = 'spam'
# print(a, b, c)

# a = b = 0
# b = b + 1
# print(a, b) 

# a = b = []
# b.append(42)
# print(a, b)

# Augmented Assignments
# X += Y X &= Y X -= Y X |= Y
# X *= Y X ^= Y X /= Y X >>= Y
# X %= Y X <<= Y X **= Y X //= Y
# X = 1
# Y = 2
# X //= Y
# print(X)

# L = [1, 2]
# L = L + [3]     # Concatenate: slowe
# L.append(4)     # Faster, but in-place
# L = L + [5, 6]          # Concatenate: slower
# L.extend([7, 8])        # Faster, but in-place
# print(L)

# print('Hi', 'My', 'Friend!', sep=', ')      # Custom separator
# print('Hi', 'My', 'Friend!', end='\2')
# print('Hi', 'My', 'Friend!', sep=', ', file=open('data.txt', 'w'))
# print(open('data.txt').read())

# text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
# print(text)

# import sys
# # sys.stdout.write('Hello World\n') # Printing the hard way
# # X = 20
# # Y = 10
# # sys.stdout.write(str(X) + ' ' + str(Y) + '\n')
# temp = sys.stdout                   # Save for restoring later
# sys.stdout = open('log.txt', 'a')   # Redirect prints to a file
# # print('spam')                       # Prints go to file, not here
# # print(1, 2, 3)
# a= '#' * 20
# L=[]
# for c in a: L.append(c)
# # print(b)
# while L:
#     # front, *L = L
#     *L , head = L
#     # print(front, L)
#     print(L, head)
# sys.stdout.close()                      # Flush output to disk
# sys.stdout = temp                       # Restore original stream
# print('back here')                      # Prints show up here again
# print(open('log.txt').read())           # Result of earlier prints


# L = []
# x = int(input('Enter a Number: '))
# while x / 2 != 0:
#     if x % 2 == 1:
#         L.append(1)
#         x = (x - 1) / 2
#     elif x % 2 == 0:
#         L.append(0)
#         x = x / 2
#     L.reverse()
#     # print(L)
# # else:
# #     print(L.append(1))
    
# print(L)
# for char in L:
#     print(char, end='')

# ['#', '#', '#', '#', '#', '#'] # # ['#', '#', '#', '#', '#', '#'] #
# x = int(input('Enter A Number: '))
# while x / 2 != 0:
#     if x % 2 == 1:
#         print(1, end='')
#         x = (x - 1)/2
#     elif x % 2 == 0:
#         print(0, end='')
#         x = x / 2
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺           write method as a file object   ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.

# log = open('log.txt', 'w')
# print(' Name '.center(20, '\2'), ' Age '.center(20, '\3'), ' Gender '.center(20, '\v'), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# print('Abdo'.center(20, ' '), '32'.center(20, ' '), 'Male'.center(20, ' '), file=log)
# log.close()
# print(open('log.txt').read())

# exl = open('log.xlsx', 'w')
# print(' Name ', ' Age ', ' Gender ', file=exl)
# exl.close()
# print(open('log.xlsx').read())

#364 page
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺                                       ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺           write method as a file object   ♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺
# ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥                                       ☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥☺♥.
# def min1(*args):
#     min = args[0]
#     for arg in args[1:]:
#         if arg < min:
#             min = arg
#     return print(min)

# min1(3,5,45,-45)

# def min2(first, *rest):
#     for arg in rest:
#         if arg < first:
#             first = arg
#     return print(first)


# min2(3,5,45,-45)

# def min3(*args):
#     tmp = list(args)
#     tmp.sort()
#     return print(tmp[0])

# min3(3,5,45,-45)

# min1('aa','dd','cc','ba')
# min2('aa','dd','cc','ba')
# min3('aa','dd','cc','ba')
# # class minmax:
# def min(*args):
#         min = args[0]
#         for arg in args[1:]:
#             if arg < min:
#                 min = arg
#         return f'the min is : {min}'            
#     # print(min(1,45,6,78,8))


# def max(*args):
#         max = args[-1]
#         for arg in args[:-1]:
#             if arg > max:
#                 max = arg
#         return f"the max is : {max}"

#     # print(max(1,4,75,84,75,96,-1))


# def minmax(test, *args):
#     res = args[0]
#     for arg in args[1:]:
#         if test(arg, res):
#             res = arg
#     return res

# def lessthan(x,y): return x < y
# def grtrthan(x,y): return x > y

# print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
# print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

# def intersect(*args):
#     res = []
#     for x in args[0]:
#         for y in args[1:]:
#             if x not in y: break
#             else:
#                 res.append(x)
#     return print(res)

# intersect((1,2), (3,4))
# intersect('span', 'scan')
# intersect('span1', 'scan')


# def union(*args):
#     res = []
#     for seq in args:
#         for x in seq:
#             if not x in res:
#                 res.append(x)
#     return print(res)

# union((1,2), (3,4))
# union('span', 'scan')
# union('span1', 'scan')

# import sys 

# def print30(*args, **Kargs):
#     sep = Kargs.get('sep', ' ')
#     end = Kargs.get('end', '\n')
#     file = Kargs.get('file', sys.stdout)
#     output = ''
#     first = True
#     for arg in args:
#         output += ('' if first else sep) + str(arg)
#         first = False
#     file.write(output + end)
        

# print30(1, 2, 3)
# print30(1, 2, 3, sep='')
# print30(1, 2, 3, sep='\3', end='.\n', file=sys.stderr)

# def mysum(L):
#     if not L:
#         return 0
#     else:
#         return L[0] + mysum(L[1:])
    
# print(mysum([1, 2, 3]))


# def mysum(L):
#     print(L)
#     if not L:
#         return 0
#     else:
#         return L[0] + mysum(L[1:])
    
# print(mysum([1, 2, 3]))

# def mysum(L):
#     return 0 if not L else L[0] + mysum(L[1:])

# def mysum(L):
#     return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

# def mysum(L):
#     first, *rest = L
#     return first if not rest else first + mysum(rest)
            
# Loop Statements Versus Recursion
# L = [12, 8, 78, 96]
# sum = 0
# while L:
#     sum += L[0]
#     L = L[1:]
# print(sum)


# L = [12, 8, 78, 96]
# sum = 0
# for x in L: sum += x
# print(sum)
# 520/1214


# Handling Arbitrary Structures
# def sumtree(L):
#     tot = 0
#     for x in L:
#         if not isinstance(x, list):
#             tot += x
#         else:
#             tot += sumtree(x)
#     return tot

# L = [1, [2, [3, 4], 5], 6, [7, 8]]

# print(sumtree(L))
# print(sumtree([1, [2, [3, [4, [5]]]]]))
# print(sumtree([[[[[1], 2], 3], 4], 5]))

# Indirect Function Calls
# def echo(message):
#     print(message)
    
# echo('Hello,World!')

# x = echo
# x('Hello, My Son!') #Indirect call!

# def indirect(func, arg):
#     func(arg)
    
# indirect(echo, 'Hi!')

# schedule = [(echo, 'Hello!'), (echo, 'Hi!')]

# for (func, arg) in schedule:
#     func(arg)
    
    
# def make(label):
#     def echo(message):
#         print(label + ':' + message)
#     return echo

# F = make('Hello')
# F('Hi!')
#Function Annotations in 3.0

# def func(a, b, c):
#     return a + b + c

# print(func(1, 2, 3))


# def func(a= 'Hi!', b = (1, 10), c= float) -> int:
#     return a + b + c

# def func(a= 'Hi!', b = (1, 10), c= float) -> int:
#     return a + b + c

# # print(func(1, 2, 3))
# print(func.__annotations__)
    
# def func(x, y, z): return x + y + z

# func(2, 3, 4)

# f = lambda x, y, z: x + z + y
# f(1, 5, 6)

# def knights():
#     title = 'Sir'
#     action = (lambda x: title + ' ' + x)
#     return action

# act = knights()
# print(act('abdo'))

# L = [lambda x: x ** 2,
#      lambda x: x **3,
#      lambda x: x **4]

# for f in L:
#     print(f(2))
    
# def f1(x): return x ** 2 + 1
# def f2(x): return x ** 3 + 2
# def f3(x): return x ** 4 + 3

# L = [f1, f2, f3]
# for f in L:
#     print(f(2))
    
# print(L[0](3))

# import sys
# from tkinter import Button, mainloop # Tkinter in 2.6
# x = Button(
# text ='Press me',
# command=(lambda:sys.stdout.write('Spam\n')))
# x.pack()
# mainloop()


# class MyGui:
#     def makewidgets(self):
#         Button(command=(lambda: self.onPress("spam")))
#     def onPress(self, message):
#         print("hello")

# Mapping Functions over Sequences:

# counters = [1,2,3,4,5,6]

# updated = []
# for x in counters:
#     updated.append(x + 10)
    
# print(updated)

# print(list(map((lambda x: x +3), counters)))




# def mymap(func, seq):
#     res = []
#     for x in seq: res.append(func(x))
#     return res

# def mymap(func , seq):
#     res = []
#     for x in seq: res.append(func(x))
#     return res

# print(mymap((lambda x: x - 1), [2, 3, 5]))

# ######## Functional Programming Tools: filter and reduce####
# print(list(range(-5, 5)))

# res = []
# for x in range(-5, 5):
#     if x < 0:
#         res.append(x)
# print(res)

# print(list(filter((lambda x: x > 0), range(-3, 6))))

# L = [1, 2, 3, 4]
# res = L[0]
# for x in L[1:]:
#     res = res + x
    
# print(res)

# sum = 0
# for x in L:
#     sum += x
#     print(sum)

# def myreduce(func, sequence):
#     first = sequence[0]
#     for next in sequence[1:]:
#         first = func(first, next)
#     return first

# print(myreduce((lambda x, y: x + y ), [1,20,45,25,14]))
# print(myreduce((lambda x, y: x * y ), [1,20,45,25,14]))

# import operator, functools
# print(functools.reduce(operator.add, [2, 4, 6]))
# print(functools.reduce((lambda x, y: x + y), [2, 4, 6]))

#################List Comprehensions Versus map#######################################
# print(ord('s')) ord func return the ASCII integer code of character

# res = []

# for x in 'sapm!':
#     res.append(ord(x))
    
# print(res)

# res = list(map(ord, 'spam'))
# print(res)

# print([x ** 2 for x in range(10)])
# print(list(map((lambda x: x ** 2), range(10))))
################################Adding Tests and Nested Loops: filter########################################
# print([x for x in range(5) if x % 2 == 0])
# print(list(filter((lambda x: x % 2 == 0), range(5))))
# res = []
# for x in range(5):
#     if x % 2 == 0:
#         res.append(x)
# print(res)

# print([x ** 2 for x in range(10) if x % 2 == 0])
# print(list( map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# res = [x + y for x in [0,1,2] for y in [100, 200, 300]]
# print(res)

# res = []
# for x in [0,1,2]:
#     for y in [300,200,100]:
#         res.append(x + y)
        
# print(res)
# print([x + y for x in 'spam' for y in 'SPAM'])
# print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

# res = []
# for x in range(5):
#     if x % 2 == 0:
#         for y in range(5):
#             if y % 2 == 1:
#                 res.append((x, y))
                
# print(res)
##############List Comprehensions and Matrixes#############
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

# print(M[1])
# print(M[1][0])

# for row in M:
#     print(row)
    
# print([row[1] for row in M])

# print([M[row][1] for row in (0, 1, 2)])

# print([M[i][i] for i in range(len(M))])

# print( [M[row][col] * N[row][col] for row in range(3) for col in range(3)] )
# print( [[M[row][col] * N[row][col] for row in range(3)] for col in range(3)] )

# res = []
# for row in range(3):
#     tmp = []
#     for col in range(3):
#         tmp.append(M[row][col] * N[row][col])
#     res.append(tmp)
    
# print(res)
#################Comprehending List Comprehensions######################################

# def gensquares(N):
#     for i in range(N):
#         yield i ** 2
        
# for i in gensquares(5):
#     print(i, end=" : ")
    
# x = gensquares(4)
# print(x)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))  Traceback (most recent call last):

# def buildsquares(n):
#     res = []
#     for i in range(n): res.append(i ** 2)
#     return res

# for x in buildsquares(5): print(x, end=' : ')

# for x in [n ** 2 for n in range(5)]:
#     print(x, end=" : ")
    
# for x in map((lambda n: n**2), range(5)):
#     print(x, end=" : ")
    
# def gen():
#     for i in range(10):
#         X = yield i 
#         print(X)
        
# G = gen()
# print(next(G))
# G.send(11)
# print(next(G))
# G.send(22)
# print(next(G))
# G.send(33)
# print(next(G))
# G.send(44)
# print(next(G))
# G.send(55)
# print(next(G))

# for num in (x ** 2 for x in range(4)):
#     print('%s, %s' % (num, num/2.0))
# print(sum(x ** 2 for x in range(4)))
# print(sorted(x **2 for x in range(10)))
# print(sorted((x ** 2 for x in range(4)), reverse=True))

# import math
# print(list( map(math.sqrt, (x ** 2 for x in range(4)))))
#########################Generator Functions Versus Generator Expressions
# G = (c * 4 for c in 'spam')
# print(list(G))

# def timesfour(S):
#     for c in S:
#         yield c * 4
        
# G = timesfour('spam')
# print(list(G))

# G = (c * 4 for c in 'spam')
# I = iter(G)
# print(next(I))

# print(iter(G) is G)

# I1 = iter(G)
# print(next(I1))

# print(list(I1))
######################Emulating zip and map with Iteration Tools################
# S1 = 'abc'
# S2 = 'xyz123'
# print(list(zip(S1, S2)))
# print( list ( zip([-2, -1, 0, 1, 2])))
# print(list(zip([1,2,3], [4,5,6])))
# print(list(map(abs, [-1,-2,-3,1,2,3,5])))
# print(list(map(pow, [1, 2, 3], [4,5,6,7,8])))

# def mymap(func, *seqs):
#     res = []
#     for args in zip(*seqs):
#         res.append(func(*args))
#     return res

# print(mymap(abs, [-2, -3, 1, 0, 8, 9]))
# print(mymap(pow, [1,2,3], [4,5,6,7,8]))

# def mymap(func, *seqs):
#     return [func(*args) for args in zip(*seqs)]

# print(mymap(abs, [-2, -3, 1, 0, 8, 9]))
# print(mymap(pow, [1,2,3], [4,5,6,7,8]))

# def mymap(func, *seqs):
#     res = []
#     for args in zip(*seqs):
#         yield func(*args)

# print(mymap(abs, [-2, -3, 1, 0, 8, 9]))
# print(mymap(pow, [1,2,3], [4,5,6,7,8]))

# def mymap(func, *seqs):
#     return (func(*args) for args in zip(*seqs))

# print(mymap(abs, [-2, -3, 1, 0, 8, 9]))
# print(mymap(pow, [1,2,3], [4,5,6,7,8]))


########Coding your own zip(...) and map(None, ...)
# print(list(map(None, [1, 2, 3], [2, 3, 4, 5])))
# print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))
# print(list(zip([1, 2, 3], [2, 3, 4, 5]) ))

# def myzip(*seqs):
#     seqs = [list(S) for S in seqs]
#     res = []
#     while all(seqs):
#         res.append(tuple(S.pop(0) for S in seqs))
#     return res

# def mymapPad(*seqs, pad =None):
#     seqs = [list(S) for S in seqs]
#     res = []
#     while any(seqs):
#         res.append(tuple((S.pop(0) if S else pad) for S in seqs))
#     return res

# S1, S2 = 'abc', 'xyz123'
# print(myzip(S1, S2))
# print(mymapPad(S1, S2))
# print(mymapPad(S1, S2, pad=99))


# print(list(S1).pop(0))
# print(list(S1))

# def myzip(*seqs):
#     seqs = [list(S) for S in seqs]
#     while all(seqs):
#         yield tuple(S.pop(0) for S in seqs)

# def mymapPad(*seqs, pad =None):
#     seqs = [list(S) for S in seqs]
#     while any(seqs):
#         yield tuple((S.pop(0) if S else pad) for S in seqs)
        
# S1, S2 = 'abc', 'xyz123'
# print(list(myzip(S1, S2)))
# print(list(mymapPad(S1, S2)))
# print(list(mymapPad(S1, S2, pad=99)))        

# def myzip(*seqs):
#     minlen = min(len(S) for S in seqs)
#     return [tuple(S[i] for S in seqs) for i in range(minlen)]

# def mymapPad(*seqs, pad=None):
#     maxlen = max(len(S) for S in seqs)
#     index = range(maxlen)
#     return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]

# S1, S2 = 'abc', 'xyz123'
# print(myzip(S1, S2))
# print(mymapPad(S1, S2))
# print(mymapPad(S1, S2, pad=99))

# def myzip(*args):
#     iters = map(iter, args)
#     while iters:
#         res = [next(i) for i in iters]
#         yield tuple(res)
# print(list(myzip('abc', 'lmnop')))

################Value Generation in Built-in Types and Classes
# D = {'a':1, 'b':2, 'c':3}
# x = iter(D)
# print(next(x))
# print(next(x))
# print(next(x))
###############Timing Module #############################

# import time 
# reps = 1000
# repslist = range(reps)

# def timer(func, *pargs, **kargs):
#     start = time.clock()
#     for i in repslist:
#         ret = func(*pargs, **kargs)
#     elapsed = time.clock() - start
#     return (elapsed, ret)

#########################Classes and OOP################################

# class C1:
#     def __init__(self, who):
#         self.name = who
        
# I1 = C1('bob')
# I2 = C1('mel')

# print(I1.name)

######################################Test #################################
print("{:0>8}".format(20))
    











