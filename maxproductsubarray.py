class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, a):
        ans = a[0]
        prev_max_product = a[0]
        prev_min_product = a[0]
        curr_max_product = a[0]
        curr_min_product = a[0]

        for i in range(1, len(a)):
            curr_min_product = min(prev_max_product * a[i], prev_min_product * a[i], a[i])
            curr_max_product = max(prev_max_product * a[i], prev_min_product * a[i], a[i])

            ans = max(ans, curr_max_product)
            prev_max_product = curr_max_product
            prev_min_product = curr_min_product
        return ans