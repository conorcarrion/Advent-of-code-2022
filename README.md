# Advent-of-code-2022

from https://adventofcode.com/2022/

An advent calendar of coding problems. 

These code problems were completed by myself, only using google to find techniques to implement my solution. 

### Day 1 

Learning outcome: Use sorted() to sort a list with argument (reverse=True) to find the highest numbers in a list

sorted(list, reverse=True)

### Day 2

Learning outcome: Use dictionaries to decode, to create scores for certain results or to decide winner between two inputs.


opp_choice = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}

my_choice = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

weapon_choice = {'rock': 1, 'paper': 2, 'scissors': 3}

resolution = {'rock': 'scissors', 
                'scissors': 'paper',
                 'paper': 'rock'}

scoring = {'lose': 0, 'draw': 3, 'win': 6}

### Day 3

Learning outcome: 
import string provides commonly used strings such as the alphabet. 
zip() is useful for putting together a dictionary or list of tuples made of 'zipping' together the matching index of two lists.
you can turn a string to a list with [*string]
you can merge two dicts with {**dict1, **dict2}. Note that if there are conflicting keys in the two dictionaries, the values from the second dictionary will overwrite those from the first dictionary.


ascii_lower_prio = dict(zip(string.ascii_lowercase, range(1,27)))
ascii_upper_prio = dict(zip(string.ascii_uppercase, range(27,53)))

alphabet = {**ascii_lower_prio, **ascii_upper_prio}

### Day 4

Learning outcome:

to compare if one range is a subset of another range, you can convert them both to sets, then use 'set1.issubset(set2) or set2.issubset(set1)'

to convert a range between m and n to a set you can use:

set1 = set(range(int(m), int(n) +1))

to see if there is any intersection at all between set1 and set2, you can use:

set1.intersection(set2) 