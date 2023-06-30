
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
        self.end="#"


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for char in word:
            node=node.setdefault(char,{})
        node[self.end]=None


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for char in word:
            if char not in node:
                return False
            node=node[char]

        return self.end in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for char in prefix:
            if char not in node:
                return False
            node=node[char]
        return True





obj = Trie()
word="apple"
prefix="app"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
param_4=obj.search(prefix)

obj.insert(prefix)
param_5=obj.search(prefix)

print(param_2,param_3,param_4,param_5)
