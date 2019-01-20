# Given a list of words, return the shortest unique prefix of each word. For
# example, given the list:

# •	dog
# •	cat
# •	apple
# •	apricot
# •	fish

# Return the list:

# •	d
# •	c
# •	app
# •	apr
# •	f

class Node:
    def __init__(self, char, word=None, path=None):
        self.char = char
        self.word = word
        self.path = path if path else {}

class Dictionary:
    def __init__(self):
        self.root = Node('')

    def build_from_words(self, words):
        for word in words:
            self.add_word(word)

    def add_word(self, word, index=0, node=None):
        node = node if node else self.root
        for i, char in enumerate(word[index:], index):
            if node.word is None:
                if char not in node.path:
                    node.path[char] = Node(char, word)
                    break
                node = node.path[char]
            else:
                print('Conflict: {} @{}@ {}'.format(word, node.char, node.word))
                pre_word = node.word
                node.word = None
                self.add_word(pre_word, i, node)
                self.add_word(word, i, node)
                break

    def shortest_prefix(self, node=None, prefix=None):
        node = node if node else self.root
        prefix = prefix if prefix is not None else ''
        prefix += node.char
        if node.word:
            print('[--> {}: {}'.format(prefix, node.word))

        for c in node.path:
            self.shortest_prefix(node.path[c], prefix)

    def display(self, node=None):
        node = node if node else self.root
        print('node<{}, {}>'.format(node.char, node.word))
        for c in node.path:
            self.display(node.path[c])


if __name__ == "__main__":
    words = ['dog', 'cat', 'apple', 'apricot', 'fish', 'approve']
    d = Dictionary()
    d.build_from_words(words)
    d.shortest_prefix()
