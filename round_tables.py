



# test



np = 150
nt = 15
ts = 10

#to track all people met all people
# for all rounds:
# for each person - did he meet person num x and table at thsi round
# {1 : [[tables visited, in place 0 the one in this], [numbers as the number of people. initialized to all -1]]} -1 means - the person was not met

#d = { 1  : [[0],[-1,-2,-3,-4]] }
 



d = {}
for i in range(0,np):
    d[i] = [[-1],[-1 for x in range(0,np)]]



print("something")

