from typing import List


def permutation(s: str) -> List[str]:
    if not s:
        return []

    s_list = list(s)

    res = []

    visited = [0] * len(s_list)

    def dfs(depth, path):

        if depth == len(s_list):
            res.append("".join(path))
            return

        for i in range(0, len(s_list)):
            char = s_list[i]
            if visited[i]:
                continue
            if i > 0 and s_list[i - 1] == char and not visited[i - 1]:
                continue

            visited[i] = 1
            dfs(depth + 1, path + [char])
            visited[i] = 0

    dfs(0, [])

    return res

s = "suvyls"
print(permutation(s))