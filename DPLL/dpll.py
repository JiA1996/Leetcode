import copy

class dpll:
    def __init__(self):
        self.clauses = []
        self.atomMap = {}
        self.numOfatoms = 0
        self.answer = None
        self.rest = []

    def run(self):
        self.readInput()
        bindings = ["placeholder"]
        for i in range(self.numOfatoms):
            bindings.append(None)
        clauses = self.clauses[:]
        self.answer = self.dplll(clauses,bindings)
        self.writeOut()

    def readInput(self):
        with open('front_out.txt') as file:
            #read clauses
            while True:
                line = file.readline().rstrip('\n')
                if not line or line == "0":
                    break
                self.clauses.append([int(atom) for atom in line.split()])
            self.rest = file.readlines()
        file.close()

        countset = []
        for clause in self.clauses:
            for atom in clause:
                if atom < 0:
                    if -1 * atom not in countset:
                        countset.append(-1 * atom)
                else:
                    if atom not in countset:
                        countset.append(atom)
        self.numOfatoms = len(countset)

    def dplll(self, Clauses, bindings):

        while True:
            if not Clauses:
                for i in range(1, len(bindings)):
                    if bindings[i] is None:
                        bindings[i] = True
                return bindings

            for c in Clauses:
                if not c:
                    return None

            atomList = []
            for c in Clauses:
                for atom in c:
                    atomList.append(atom)
            #print(atomList)

            single = False
            for c in Clauses:
                if len(c) == 1:
                    if c[0] > 0:
                        Clauses = self.propagate(c[0], Clauses, bindings, True)
                    else:
                        Clauses = self.propagate(-1*c[0], Clauses, bindings, False)
                    single = True
                    break
            if single:
                continue

            deleted = False
            for atom in atomList:
                #pure
                if (-1 * atom) not in atomList:
                    if atom > 0:
                        bindings[atom] = True
                    else:
                        bindings[-1 * atom] = False
                    for i in range(0, len(Clauses)):
                        if atom in Clauses[i]:
                            Clauses.pop(i)#***********
                            break
                    # print(Clauses)
                    # print(atom)
                    deleted = True
                    break
            if deleted:
                continue
            #no easy case
            break

        for i in range(1, len(bindings)):
            if bindings[i] is None:
                C_copy, b_copy = copy.deepcopy(Clauses), copy.deepcopy(bindings)
                C_copy2 = self.propagate(i, Clauses, bindings, True)
                ans = self.dplll(C_copy2, bindings)
                if ans is not None:
                    return ans
                c1, b1 = C_copy[:], b_copy[:]
                C_copy3 = self.propagate(i, c1, b1, False)
                return self.dplll(C_copy3, b1)

    def propagate(self, atom, Clauses, bindings, tf):
        bindings[atom] = tf
        toDelete = []
        t = 0
        if tf:
            t = 1
        else:
            t = -1
        for i in range(len(Clauses)):
            c = Clauses[i]
            if atom in c and bindings[atom] is True:
                toDelete.append(i)
                continue
            if (-1 * atom) in c and bindings[atom] is False:
                toDelete.append(i)
                continue
            for j in range(len(c)):
                if c[j] == atom and bindings[atom] is False:
                    Clauses[i].pop(j)
                    break
                if c[j] == (-1 * atom) and bindings[atom] is True:
                    Clauses[i].pop(j)
                    break
        for x in reversed(toDelete):
                Clauses.pop(x)
        return Clauses

    def writeOut(self):
        Lines = []
        if self.answer is not None:
            for i in range(1, len(self.answer)):
                    if self.answer[i]:
                        Lines.append(str(i) + ' T' + '\n')
                    else:
                        Lines.append(str(i) + ' F' + '\n')
        file = open("dpll_out.txt", "w")
        file.writelines(Lines)
        file.writelines("0\n")
        file.writelines(self.rest)
        file.close()


if __name__ == '__main__':
    sol = dpll()
    sol.run()