class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):

        last = len(A) - 1
        jumps = 0
        reachable = 0  # reachable with current number of jumps
        next_reachable = 0  # reachable with one additional jump
        for i, x in enumerate(A):

            if reachable >= last:
                break

            if reachable < i:
                reachable = next_reachable
                jumps += 1
                if reachable < i:
                    return -1
            next_reachable = max(next_reachable, i + x)

        return jumps
