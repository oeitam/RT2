
#to track all people met all people
# for all rounds:
# for each person - did he meet person num x and table at thsi round
# {1 : [[tables visited, in place 0 the one in this], [numbers as the number of people. initialized to all -1]]} -1 means - the person was not met, -2 is same person

#d = { 1  : [[0],[-1,-2,-3,-4]] }
 
# NOTE: need to mark people from 0, to easily reference in the list location

class RT:
    def __init__(self, np, nt, ts):
        self.np = np # number of people
        self.nt = nt # number of tables
        self.ts = ts # table size
        self.d = {}
        self.rn = 0 # round number
        self.last_person_checked_if_sitted = -1
        self.persons_already_sitted_in_this_round = 0

        # create the dict data structure
        for p in range(0,self.np):
            print(p)
            ##self.d[p] = [[],[-1 for x in range(0,self.np)]] # first list is table in each round. second list is whom a person sat with
            self.d[p] = [[],[-1]*self.np] # first list is table in each round. second list is whom a person sat with
                                                            # note that if say with all - there is no '-1' in this list
            self.d[p][1][p] = -2 # no one sits with himself
        print(self.d)

    def who_is_at_this_tbl(self, tbl):
        #l = [x for x in self.d.keys() if self.d[x][0][self.rn-1] == tbl]
        l = [x for x in self.d.keys() if self.d[x][0][0] == tbl]
        print(f"tbl {tbl} l {l}")
        return l
    
    def find_next_person_did_not_sit_with(self,pl): # pl is a list of people
        # will return the next person that p did not sit with any person on 
        # the list pl
        ln = len(pl)
        if ln < 1 :
            return -1
        # get sub dictionary for pl
        #d1 = {k:self.d[k] for k in pl if k in self.d}
        l1 = [self.d[z][1] for z in pl] # create a list of all the lists of sitting together for all of the people in pl
        l2 = list(zip(*l1[:])) # zip the lists together so we can look for index that is all -1
        try:
            i = l2.index(tuple(-1 for x in range(0,len(pl)))) # find an index that is all -1 for all (all did not meet this person) by creating  tuple that long
        except:
            return -1
        return i

    def did_person_sit_with_people_at_this_table(self, p, lop):
        # did p sat with anyone in lop (even with one of them is enoug)
        ret = False
        if len(lop) == 0:
            return ret
        for m in lop:
            if self.d[m][1][p] != -1: # 
                ret = True
        return ret


    def sit(self, p, tbl, lop):
        # check if can sit
        ret = True
        for m in lop: # update for p he sat with people in lop, and update for people in lop they say with person P
            if self.d[p][1][m] != -1:
                ret = False
            if self.d[m][1][p] != -1:
                ret = False
        if ret : # is true
            self.d[p][0][0] = tbl # put p in the table
            for m in lop: # update for p he sat with people in lop, and update for people in lop they say with person P
                self.d[p][1][m] = 1
                self.d[m][1][p] = 1
        if ret:
            self.persons_already_sitted_in_this_round += 1
        return ret

    def get_the_next_person_who_is_not_seated_in_this_round(self):
        #returns the next person who is not yet seated in this round
        lp = self.last_person_checked_if_sitted+1 # add one, otherwise we may stuck in a look. Staart looking from teh next
        if lp == -1 : # first time we use this
            self.last_person_checked_if_sitted = 0
            return 0 # use the first person 
        l = [self.d[x][0][0] for x in range(0,self.np)] # list of -1 if not sitted, or # of the round
        if not (-1 in l) : # if all are sitted 
            return -1
        ind = (l[lp:]+l[:lp]).index(-1) # rotating the list to find the next not sitted person, since do not want always to try from the first one
        self.last_person_checked_if_sitted = ((lp+ind)%self.np) # use modulu division to get the 'right' person since we 'roteted' the list to fine ind
        return (self.last_person_checked_if_sitted)
                        
    def rounds(self):
        # creating the rounds
        # TODO: take care of the rounds
        while self.rn < 200: #pepotect fomr endless rounds
            self.rn += 1
            self.persons_already_sitted_in_this_round = 0
            # add a colum of '-1' in d[p][0] to support the lop parameter finding w/o errors
            for p in range(0,self.np):
                self.d[p][0].insert(0,-1)
            tbl = 1 # counts 1 to self.nt
            pattbl = 0 # counts 1 to self.ts
            while self.persons_already_sitted_in_this_round < self.np : #while still people to sit 
                p = self.get_the_next_person_who_is_not_seated_in_this_round()
                if p < 0 :
                    raise ValueError(f"how come no next person to sit and still here?")
                lop = self.who_is_at_this_tbl(tbl) # get a list of all the people at this table at this time    
                if not self.did_person_sit_with_people_at_this_table(p, lop): # can we sit p in the table? did he sit with (at least one) occupants before?
                    if self.sit(p, tbl, lop):
                        pattbl += 1
                    else:
                        raise ValueError(f"how come we failed to sit person {p} at the table {tbl} ?")
                    if pattbl == self.ts: # table is full
                        pattbl = 0
                        tbl += 1 # next table
                        if tbl > (self.nt + 1):
                            raise ValueError(f"{p} {tbl} {pattbl}")
                else:
                    self.last_person_checked_if_sitted = (self.find_next_person_did_not_sit_with(lop)-1)%self.np # if we could not sit the person, let us update teh next person to sit
                    


    def round1(self):
    # creating the rounds
        while self.rn < 200: # safe guard againts endless loop
            self.rn += 1
            # add a colum of '-1' in d[0][0] to support the lop parameter finding w/o errors
            for p in range(0,self.np):
                self.d[p][0].insert(0,-1)
            tbl = 1 # start placing people from table one. once teh table will be full, move to the next table
            pattbl = 0 # how many people sit at teh table while creating the seating
            for p in range(0,self.np):
                lop = self.who_is_at_this_tbl(tbl) # get a list of all the people at this table at this time
                #self.d[p][0].append(tbl) # added for this person that he is participatin in round rn on table tbl
                t = find_next_person_did_not_sit_with(lop) # get what is the next 
                self.d[p][0][0] = tbl # added for this person that he is participatin in round rn on table tbl
                pattbl +=1
                np = self.find_next_person_did_not_sit_with(lop)
                if len(lop) > 0 : # not sitting alonoe
                    for i in lop: #update seating
                        if self.d[p][1][i] != -1 : # was already seated with this person
                            raise ValueError(f"{p} {tbl} {pattbl} {lop} {i}")
                        self.d[p][1][i] = self.rn
                        if self.d[i][1][p] != -1 : # was already seated with this person
                            raise ValueError(f"{p} {tbl} {pattbl} {lop} {i}")
                        self.d[i][1][p] = self.rn
                if pattbl == self.ts: # table is full
                    pattbl = 0
                    tbl += 1 # next table
                    if tbl > (self.nt + 1):
                        raise ValueError(f"{p} {tbl} {pattbl}")
                    


if __name__ == '__main__':
    rt = RT(12,4,3)
    rt.rounds()
            


