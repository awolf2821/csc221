"""
>>> myseq = Seqtools([1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True])
>>> myseq.data()
[1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True]
>>> myseq.nums()
[1, 2, 7, 11.3]
>>> myseq.seqs()
['a', ('x', 'y'), 'yup']
>>> myseq.others()
[True]
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
            if isinstance(item, (numTypes)) and not isinstance(item, bool):
                numsList.append(item)
            else:
                continue
        return numsList

    def seqs(self):
        seqsList = []
        seqTypes = (str, tuple, list, dict, set)
        for item in self.list:
            if isinstance(item, (seqTypes)):
                seqsList.append(item)
        return seqsList

    def others(self):
        othersList = []
        typesList = (str, list, tuple, dict, set, int, float)
        for item in self.list:
            if not isinstance(item, (typesList)):
                othersList.append(item)
            elif isinstance(item, bool):
                othersList.append(item)
            else:
                continue
        return othersList

if __name__ == "__main__":
    import doctest
    doctest.testmod()

