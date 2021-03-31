class backEnd:

    def __init__(self):
        self.move = []
        self.correctIndex = []
        self.failed = 0

    def run(self):
        with open('dpll_out.txt') as file:
            if file.readline().rstrip('\n') == "0":
                self.failed = 1
        file.close()
        self.readInput()
        print(self.move)
        self.writeOut()

    def readInput(self):
        with open('dpll_out.txt') as file:
            while True:
                line = file.readline().rstrip('\n')
                if not line or line == "0":
                    break
                line = line.split()
                if line[1] == "T":
                    self.correctIndex.append(int(line[0]))
            while True:
                line = file.readline().rstrip('\n')
                if not line or line == "0":
                    break
                line = line.split()
                if int(line[0]) in self.correctIndex and line[1][0] == "A":
                    self.move.append(line[1])
        file.close()

    def writeOut(self):
        if self.failed:
            print("NO SOLUTION")
        else:
            Line = []
            for m in self.move:
                m = m.split(",")
                Line.append(m[0][3:])
            with open('answer.txt', "w") as file:
                file.writelines(" ".join(Line))
                file.close()




if __name__ == '__main__':
    sol = backEnd()
    sol.run()