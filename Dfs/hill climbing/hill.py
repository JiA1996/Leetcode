import collections
import sys
import random

class Solution:

    def __init__(self):
        self.cost_map = collections.defaultdict(lambda: 0)
        self.vertex_list = []
        self.edge_pair = []
        self.budget = 0
        self.verbose = None
        self.goal = 0
        self.num_of_rand = 0
        self.curr_state = None

    def readinput(self, filename):
        file = open(filename)

        # read budget and verbose
        line = file.readline()
        b, v, r = line.split()
        self.budget = int(b)
        self.num_of_rand = int(r)
        if v == "V":
            self.verbose = 1

        # read vertex and corresponding cost
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

    def get_total_cost(self, state):
        if not state:
            return 0
        res = 0
        for s in state:
            res += self.cost_map[s]
        return res

    def compute_err(self, state):
        if not state:
            res = 0
            for v1, v2 in self.edge_pair:
                res += min(self.cost_map[v1], self.cost_map[v2])
            return res
        uncovered_edge = 0
        cost = self.get_total_cost(state)
        for v1, v2 in self.edge_pair:
            if v1 not in state and v2 not in state:
                uncovered_edge += min(self.cost_map[v1], self.cost_map[v2])
        return max(0, cost - self.budget) + uncovered_edge

    def get_neighbors(self, state):
        res = []
        if state:
            for v in state:
                res.append(list(set(state) - set(v)))

        for v in self.vertex_list:
            if v not in state:
                res.append(state+[v])
        return res

    def generate_rand_state(self):
        res = []
        for i in range(len(self.vertex_list)):
            if random.randint(0, 1):
                res.append(self.vertex_list[i])
        return res

    def hill_climb(self):
        self.readinput(sys.argv[1])
        for i in range(self.num_of_rand):
            self.curr_state = self.generate_rand_state()
            found = self.random_search()
            if found:
                print('Found Solution {} Cost={}. Error={}'.format(" ".join(self.curr_state),
                                                            self.get_total_cost(self.curr_state),
                                                            self.compute_err(self.curr_state)))
                return
        print("No solution found.")

    def random_search(self):
        if self.verbose:
            print('Randomly chosen start state: {}'.format(" ".join(self.curr_state)))

        while True:
            if self.verbose:
                print('move to {} Cost={}. Error={}'.format(" ".join(self.curr_state), self.get_total_cost(self.curr_state),
                                                        self.compute_err(self.curr_state)))
            if self.compute_err(self.curr_state) == 0:
                return True

            fail = 1
            if self.verbose:
                print("Neighbors:")

            neighbors = self.get_neighbors(self.curr_state)
            for n in neighbors:
                if self.verbose:
                    if not n:
                        print('{{}} Cost={}. Error={}'.format(self.get_total_cost(n), self.compute_err(n)))
                    else:
                        print('{} Cost={}. Error={}'.format(" ".join(n), self.get_total_cost(n), self.compute_err(n)))
                if self.compute_err(n) == 0:
                    self.curr_state = n
                    return True
                if self.compute_err(n) < self.compute_err(self.curr_state):
                    self.curr_state = n
                    fail = 0
            if self.verbose:
                print("\n")
            if fail:
                if self.verbose:
                    print("Search failed")
                    print("\n")
                return False


if __name__ == '__main__':
    sol = Solution()
    sol.hill_climb()








