## This program converts a maze into clauses
## The output of this will be used as input to DPLL
import sys


class frontEnd:

    def __init__(self):
        self.nodesList = []
        self.treasureList = []
        self.maxSteps = []
        self.maze = []
        self.treasureMap = {}
        self.atomMap = {}

    def readInput(self, filename):

        with open(filename, 'r') as file:
            # read nodes
            line = file.readline()
            self.nodesList = line.split()

            # read treasures
            line = file.readline()
            self.treasureList = line.split()

            # read allowed steps
            line = file.readline()
            self.maxSteps = int(line[0])

            # read maze
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.split()
                m = []
                for element in line:
                    if element in self.nodesList:
                        m.append(element)
                if m:
                    self.maze.append(m)

                t = []
                for i in range(2, len(line)):
                    if line[i] == "NEXT":
                        break
                    t.append(line[i])
                if t:
                    self.treasureMap[line[0]] = t
        file.close()


    def printC1(self, file):
        combination = []
        def backtrace(path, i):
            if len(path) == 2:
                combination.append(path)
                return
            for j in range(i, len(self.nodesList)):
                backtrace(path + [self.nodesList[j]], j + 1)
        backtrace([], 0)
        #print(combination)

        for step_i in range(self.maxSteps + 1):
            for node1, node2 in combination:
                line = "~At(" + node1 + "," + str(step_i) + ") V ~At(" + node2 + "," + str(step_i) + ")\n"
                file.writelines(line)

    def printC2(self, file):
        for i in range(self.maxSteps):
            for m in self.maze:
                line = "~At(" + m[0] + "," + str(i) + ")"
                for j in range(1, len(m)):
                    line += (" V At(" + m[j] + "," + str(i+1) + ")")
                line += "\n"
                file.writelines(line)

    def printC3(self, file):
        for i in range(self.maxSteps + 1):
            for node, tList in self.treasureMap.items():
                for t in tList:
                    line = "~At(" + node + "," + str(i) + ") V Has(" + t + "," + str(i) + ")\n"
                    file.writelines(line)

    def printC4(self, file):
        for i in range(self.maxSteps):
            for t in self.treasureList:
                line = "~Has(" + t + "," + str(i) + ") V Has(" + t + "," + str(i+1) + ")\n"
                file.writelines(line)

    def printC5(self, file):
        for i in range(self.maxSteps):
            for t in self.treasureList:
                nodesContainTreasure = []
                for node, tList in self.treasureMap.items():
                    if t in tList:
                        nodesContainTreasure.append(node)

                line = "Has(" + t + "," + str(i) + ") V ~Has(" + t + "," + str(i + 1) + ")"
                for node in nodesContainTreasure:
                    line += " V At(" + node + "," + str(i + 1) + ")"
                line += "\n"
                file.writelines(line)

    def printC6(self, file):
        line = "At(START,0)\n"
        file.writelines(line)

    def printC7(self, file):
        for t in self.treasureList:
            line = "~Has(" + t + ",0)\n"
            file.writelines(line)

    def printC8(self, file):
        for t in self.treasureList:
            line = "Has(" + t + "," + str(self.maxSteps) + ")\n"
            file.writelines(line)

    def printClauses(self):
        self.readInput(sys.argv[1])
        file = open('front_clauses.txt', 'w')
        self.printC1(file)
        self.printC2(file)
        self.printC3(file)
        self.printC4(file)
        self.printC5(file)
        self.printC6(file)
        self.printC7(file)
        self.printC8(file)
        # print(self.nodesList)
        # print(self.treasureList)
        # print(self.maxSteps)
        # print(self.maze)
        # print(self.treasureMap)
        file.close()

    def convert(self):
        file_in = open('front_clauses.txt', 'r')
        file_out = open("front_out.txt", 'w')
        counter = 1
        while True:
            line = file_in.readline()
            if not line:
                break
            line = line.strip().split(" V ")
            line_out = ""
            for a in line:
                if a[0] == '~':
                    if a[1:] not in self.atomMap:
                        self.atomMap[a[1:]] = counter
                        self.atomMap[a] = -counter
                        counter += 1
                else:
                    if a not in self.atomMap:
                        self.atomMap[a] = counter
                        self.atomMap["~"+a] = -counter
                        counter += 1
                line_out += (str(self.atomMap[a]) + " ")
            line_out += "\n"
            file_out.writelines(line_out)
        file_out.writelines("0\n")
        for k, v in self.atomMap.items():
            line_out = []
            if int(v) < 0:
                continue
            if int(v) < 10:
                line_out += (" " + str(v) + " ")
            else:
                line_out += (str(v) + " ")
            line_out += (k + "\n")
            file_out.writelines(line_out)
        file_out.close()


    def run(self):
        self.printClauses()
        self.convert()


if __name__ == '__main__':
    app = frontEnd()
    app.run()