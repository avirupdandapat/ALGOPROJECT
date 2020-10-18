class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):

        # hashmap with sorted string as key and list of anagrams as values
        hashmap = {}

        for index, word in enumerate(A):

            # sorted() returns a list, hence first convert it to a string
            # so that we can use it as a key in the hashmap
            sorted_word = ''.join(sorted(word))

            if sorted_word not in hashmap:

                # create key if not present and associate
                # the current word with it
                hashmap[sorted_word] = [index + 1]
            else:

                # append the current word to the list associated with the key
                hashmap[sorted_word] += [index + 1]

        # hashmap.values() returns a dict_values object in python 3,
        # hence convert it into a list while returning
        return list(hashmap.values())


if __name__ == '__main__':
    A = ['cat', 'dog', 'god', 'tca']
    print(Solution().anagrams(A))
