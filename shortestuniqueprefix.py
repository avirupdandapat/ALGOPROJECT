class Node:
    def __init__(self, char=None):
        self.char = char
        self.neighbours = {}
        self.count = 0


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie_root = Node()

        for word in A:
            curr_tree_pos = trie_root
            for char in word:
                if char not in curr_tree_pos.neighbours:
                    curr_tree_pos.neighbours[char] = Node(char)

                curr_tree_pos = curr_tree_pos.neighbours[char]
                curr_tree_pos.count = curr_tree_pos.count + 1
        pref = []
        for w in A:
            curr_tree_pos = trie_root
            result_char = ''
            for ch in w:
                curr_tree_pos = curr_tree_pos.neighbours[ch]
                result_char = result_char + ch
                if curr_tree_pos.count == 1:
                    pref.append(result_char)
                    break

        return pref


if __name__ == '__main__':
    A = ["zebra", "dog", "duck", "dot"]
    print(Solution().prefix(A))
