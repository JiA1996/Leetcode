import collections
import sys

class Solution:

    def __init__(self):
        self.cost_map = collections.defaultdict(lambda: 0)
        self.vertex_list = []
        self.edge_pair = []
        self.budget = 0
        self.verbose = 0
        self.goal = 0

    def readinput(self, filename):
        file = open(filename)

        # read budget and verbose
        line = file.readline()
        b, v = line.split()
        self.budget = int(b)
        if v == 'V':
            self.verbose = 1


        # read vertext and corresponding cost
        while 1:
            line = file.readline()
            if line == "\n":
                break
            vertex, cost = line.split()
            self.vertex_list.append(vertex)
            self.cost_map[vertex] = int(cost)

        # read edges
        while 1:
            line = file.readline()
            if not line:
                break
            self.edge_pair.append(line.split())

    def check_goal(self, state):
        for v1, v2 in self.edge_pair:
            if v1 in state or v2 in state:
                continue
            return False
        return True

    def get_succsessor(self, state):

        res = []

        if not state:
            for j in range(0, len(self.vertex_list)):
                successor = state + [self.vertex_list[j]]
                res.append(successor)
            return res

        curr = state[-1]

        for i in range(0, len(self.vertex_list)):
            if self.vertex_list[i] == curr:
                break

        for j in range(i+1, len(self.vertex_list)):
            successor = state + [self.vertex_list[j]]
            res.append(successor)
        return res

    def get_total_cost(self, state):
        res = 0
        for s in state:
            res += self.cost_map[s]
        return res

    def dfs(self, state, depth, maxdepth):
        if depth > maxdepth:
            return

        if state:
            cost = self.get_total_cost(state)
            if cost > self.budget:
                return
            if self.verbose:
                print('{} Cost = {}.'.format(" ".join(state), cost))
            if self.check_goal(state):
                print('Find solution {} Cost = {}.'.format(" ".join(state), cost))
                self.goal = 1
                return

        successor = self.get_succsessor(state)
        for s in successor:
            self.dfs(s, depth + 1, maxdepth)
            if self.goal:
                return

        return 0

    def iter_deep(self):
        self.readinput(sys.argv[1])
        for i in range(1, 5):
            if self.verbose:
                print('Depth = {}'.format(i))
            ans = self.dfs([], 0, i)
            if self.goal:
                break
            if self.verbose:
                print("\n")

if __name__ == '__main__':
    sol = Solution()
    sol.iter_deep()








