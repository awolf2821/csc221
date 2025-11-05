"""
>>> myseq = Seqtools([1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True'])
>>> myseq.data()
[1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True']
>>> myseq.nums()
[1, 2, 7, 11.3]
>>> myseq.seqs()
['a', ('x', 'y'), 'yup']
>>> myseq.others()
[True']
"""

class Seqtools():

    def __init__(self, list):
        self.list = list

    def data(self):
        return self.list

    def nums(self):
        numsList = []
        numTypes = (int, float)
        for item in self.list:
            if isinstance(self.list[item], (numTypes)):
                numsList.append(self.list[item])
            else:
                continue
        return numsList

    def seqs(self):
        seqsList = []
        seqTypes = (str, tuple, list, dict, set)
        for item in self.list:
            if isinstance(self.list[item], (seqTypes)) in seqTypes:
                seqsList.append(self.list[item])
            else:
                continue
        return seqsList

    def others(self):
        othersList = []
        typesList = (str, list, tuple, dict, set)
        for item in self.list:
            if not isinstance(self.list[item], (typesList)):
                othersList.append(self.list[item])
            else:
                continue
        return othersList

if __name__ == "__main__":
    import doctest
    doctest.testmod()

