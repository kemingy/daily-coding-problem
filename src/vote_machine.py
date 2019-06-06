# On election day, a voting machine writes data in the form
# (voter_id, candidate_id) to a text file. Write a program that reads this
# file as a stream and returns the top 3 candidates at any given time.
#
# If you find a voter voting more than once, report this as fraud.

from collections import Counter


class Voting:
    def __init__(self):
        self.voters = set()
        self.candidates = Counter()

    def vote(self, voter, candidate):
        if voter in self.voters:
            print(f'Fraud: {voter} already voted.')
            return
        self.voters.add(voter)
        self.candidates.update([candidate])

    def top3(self):
        return self.candidates.most_common(3)


if __name__ == "__main__":
    v = Voting()
    for voter, cand in [('hello', 'rust'), ('hi', 'c'), ('fine', 'python'),
                        ('hello', 'world'), ('good', 'rust'),
                        ('emmmm', 'javascript')]:
        v.vote(voter, cand)
    print(v.top3())
    for voter, cand in [('easy', 'python'), ('old', 'lisp')]:
        v.vote(voter, cand)
    print(v.top3())
