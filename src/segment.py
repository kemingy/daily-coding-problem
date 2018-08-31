# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. If there is more than one possible 
# reconstruction, return any of them. If there is no possible reconstruction, 
# then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
# ['bedbath', 'and', 'beyond'].

class Node:
    def __init__(self, char, path):
        self.char = char
        self.path = path
        self.children, self.word = {}, ''


class Trie:
    def __init__(self):
        self.root = Node('', '')

    def add_word(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                new_node = Node(char, word[:i+1])
                node.children[char] = new_node
            node = node.children[char]

        node.word = word

    def segment(self, text):
        ans = []
        node = self.root
        for char in text:
            if char not in node.children:
                if node.word:
                    ans.append(node.word)
                    node = self.root
                else:
                    return None
            node = node.children[char]

        if node.word:
            ans.append(node.word)
        else:
            return None

        return ans


if __name__ == '__main__':
    t = Trie()
    for word in ['quick', 'brown', 'the', 'fox']:
        t.add_word(word)

    print(t.segment('thequickbrownfox'))

    t = Trie()
    for word in ['bed', 'bath', 'and', 'beyond', 'bedbath']:
        t.add_word(word)

    print(t.segment('bedbathandbeyond'))
