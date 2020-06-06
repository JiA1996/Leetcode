# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:
S = "ADOBECODEBANC"
T = "ABC"
# Output: "BANC"

import collections

def minWindow(s: str, t: str) -> str:

    if s == "" or t == "" or len(s) < len(t):
        return ""
    if t in s:
        return t

    # sliding window boundary
    left = 0
    right = 0

    # result
    resL = 0
    resR = len(s) + 1

    # Frequency table
    Ttable = collections.Counter(t)
    Wtable = {}

    # used to count how many elements of t exist in sliding window
    num = 0

    while right < len(s):
        right_c = s[right]
        if right_c not in Ttable: # meet a char we don't need
            right += 1            # keep moving right
            continue

        if right_c not in Wtable.keys(): # meet a char we need
            Wtable[right_c] = 1   # add to Wtable
        else:
            Wtable[right_c] += 1

        if Wtable[right_c] <= Ttable[right_c]:
            num += 1
        right += 1
        print(Wtable ,right)

        while num == len(t):      # we have all we need in window
            left_c = s[left]
            if right - left < resR - resL:
                resR = right      # update result
                resL = left
            if left_c not in Ttable:
                left += 1         # meet useless char, go left don't stop
                continue
            if Wtable[left_c] == Ttable[left_c]:
                num -= 1          # if we happened to have a perfect number of char,
                                  # and we gonna delete this char, decrease num
            Wtable[left_c] -= 1
            left += 1

    if resR == len(s) + 1:        # resR is never updated, which means there is no substring
        return ""

    return s[resL:resR]

print(minWindow(S, T))


