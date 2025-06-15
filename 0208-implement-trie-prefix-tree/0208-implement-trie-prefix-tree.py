class Tree:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_end = False

class Trie:

    def __init__(self):
        self.tree = Tree(None)

    def insert(self, word: str) -> None:
        tree = self.tree
        for char in word:
            if char not in tree.children.keys():
                tree.children[char] = Tree(char)
            tree = tree.children[char]
        tree.is_end = True

    def search(self, word: str) -> bool:
        tree = self.tree
        for char in word:
            if char not in tree.children.keys():
                return False
            tree = tree.children[char]
        return tree.is_end

    def startsWith(self, prefix: str) -> bool:
        tree = self.tree
        for char in prefix:
            if char not in tree.children.keys():
                return False
            tree = tree.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)