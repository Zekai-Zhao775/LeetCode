from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                node = node.children[char]
            else:
                node = node.children[char]
        node.is_end_of_word = True

    def prefix(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node

    def _collect(self, node: TrieNode, path: str, out: List[str]) -> None:
        if node.is_end_of_word:
            out.append(path)
        for char in sorted(node.children):
            self._collect(node.children[char], path + char, out)

    def prefixWord(self, prefix: str) -> List[str]:
        result = []
        node = self.prefix(prefix)
        if node is None:
            return []
        self._collect(node, prefix, result)
        return result

    def suggest(self, word: str) -> List[str]:
        result = self.prefixWord(word)
        if result == None:
            return result
        elif len(result) <= 3:
            return result
        else:
            return result[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        # build Trie to store all products str
        products_trie = Trie()
        for product in products:
            products_trie.insert(product)

        for i in range(len(searchWord)):
            result.append(products_trie.suggest(searchWord[:i + 1]))

        return result