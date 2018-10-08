# Implement an autocomplete system. That is, given a query string s and a set of 
# all possible query strings, return all strings in the set that have s as a 
# prefix.
# For example, given the query string de and the set of strings 
# [dog, deer, deal], return [deer, deal].

class Node:
    def __init__(self, char):
        self.char = char
        self.words = []
        self.children = {}


class Trie:
    def __init__(self, words):
        self.root = Node(None)
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]

        node.words.append(word)

    def search(self, word):
        ans = []
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]

        level = [node]
        while level:
            children = []
            for n in level:
                ans.extend(n.words)
                children.extend(n.children.values())

            level = children

        return ans


class AutoComplete:
    def __init__(self, words):
        self.trie = Trie(words)

    def search(self, text):
        return self.trie.search(text)



if __name__ == '__main__':
    ac = AutoComplete(['dog', 'deal', 'deer'])
    print(ac.search('de'))
    print(ac.search('d'))
    print(ac.search('dd'))
