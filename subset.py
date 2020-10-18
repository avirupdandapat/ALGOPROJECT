class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse=True)
        results = [[]]
        while A:
            n = A.pop()
            print(n)
            temp = []
            for result in results:
                print('result', result)
                temp.append(result + [])
                print('temp1', temp)
                temp.append(result + [n])
                print('temp2', temp)
            results = temp
        results.sort()
        return results


if __name__ == '__main__':
    A = [1, 2, 3]
    print(Solution().subsets(A))