# Write an algorithm to justify text. Given a sequence of words and an integer 
# line length k, return a list of strings which represents each line, fully 
# justified.

def justify(words, max_width):
    if not words:
        return ['']

    lines = [[words[0]]]
    length = []
    cur_len = len(words[0])
    
    for w in words[1:]:
        if cur_len + len(w) < max_width:
            cur_len += len(w) if cur_len == 0 else 1 + len(w)
            lines[-1].append(w)
        else:
            lines.append([w])
            length.append(cur_len)
            cur_len = len(w)

    length.append(cur_len)

    ans = []
    for i, line in enumerate(lines):
        slot = len(line) - 1
        space = max_width - length[i] + slot

        if slot == 0 or i == len(lines) - 1:
            ans.append(' '.join(line) + ' ' * (space - slot))
        else:
            if space % slot == 0:
                mean_space = int(space / slot)
                ans.append((mean_space * ' ').join(line))
            else:
                mean_space = int(space // slot)
                remainder = space - slot * mean_space
                text = line[0]
                for index, word in enumerate(line[1:]):
                    if index < remainder:
                        text += ' ' * (mean_space + 1) + word
                    else:
                        text += ' ' * mean_space + word
                
                ans.append(text)

    return ans


if __name__ == '__main__':
    for words, width in [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["Science","is","what","we","understand","well","enough","to","explain",
            "to","a","computer.","Art","is","everything","else","we","do"], 20),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (["Listen","to","many,","speak","to","a","few."], 6),
    ]:
        for line in justify(words, width):
            print('[{}] - "{}"'.format(len(line), line))
        print('-' * 80)
