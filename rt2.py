# take two

'''
You can use the following Python code to divide 150 people into groups of 10 each time until each person was in a group with each other person from the 150 people at least once:

python
from itertools import combinations

people = range(1, 151)
groups = [people[i:i+10] for i in range(0, len(people), 10)]

for i in range(15):
    print(f"Round {i+1}:")
    for group in groups:
        for pair in combinations(group, 2):
            print(pair)
    groups = [list(set().union(*pair)) for pair in combinations(groups, 2)]


This code uses the `itertools.combinations()` function to generate all possible pairs of people within each group. It then combines each pair of groups to form new groups until each person has been in a group with each other person from the 150 people at least once. 

I hope this helps! Let me know if you have any questions.

Source: Conversation with Bing, 6/9/2023
(1) python - How do I split a list into equally-sized chunks? - Stack Overflow. https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks.
(2) Alternative way to split a list into groups of n [duplicate]. https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n.
(3) Number of ways to divide $n$ people into $2$ distinct groups, with at .... https://math.stackexchange.com/questions/4047678/number-of-ways-to-divide-n-people-into-2-distinct-groups-with-at-least-1.
'''

from itertools import *

np = 36
nt = 6
ts = 6

k = 0

# round 1
r11 = list(combinations(range(0,np),ts))
master = r11.copy() # save
r12 = [x for x in r11 if len(set(r11[0]).union(set(x))) == 2*ts-k]
print(len(r12))
r13 = [x for x in r12 if len(set(r12[0]).union(set(x))) == 2*ts-k]
print(len(r13))
r14 = [x for x in r13 if len(set(r13[0]).union(set(x))) == 2*ts-k]
print(len(r14))
print(f"{r11[0]} {r12[0]} {r13[0]} {r14[0]}")
round1 = (r11[0],r12[0], r13[0], r14[0])
 # round 2

k = ts/2

r21 = [x for x in r11 if len(set(round1[0]).union(set(x))) == 2*ts-k]
print(r12[0])
r22 = [x for x in r11 if len(set(round1[1]).union(set(x))) == 2*ts-k]
print(r22[0])


list(c2)
