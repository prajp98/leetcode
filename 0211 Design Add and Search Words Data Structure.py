class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def f(index,node):
            for i in range(index,len(word)):
                char=word[i]
                if char==".":
                    for child in node.children.values():
                        if f(i+1,child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node=node.children[char]
            return node.end
        return f(0,self.root)