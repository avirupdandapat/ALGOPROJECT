class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, num_stairs):
        if num_stairs < 2:
            return num_stairs

        ways = [0 for i in range(num_stairs)]
        ways[0] = 1 # First step can be climbed only in one way
        ways[1] = 2 # Second step can be reached from ground or first step directly

        # Step i can be reached directly from i-1 or i-2.
        for i in range(2, num_stairs):
            ways[i] = ways[i-1]+ways[i-2]

        return ways[-1]