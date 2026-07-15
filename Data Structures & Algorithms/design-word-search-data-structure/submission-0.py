class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            node = root
        
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in node.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if word[j] not in node.children:
                        return False
                    node = node.children[word[j]]

            return node.endOfWord
        return dfs(0, self.root)   

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False