from collections import Counter

class AbstractOne:
    def __init__(self, address):
        self.address = address


    def calculateFreqs(self):
        pass








class ListCount(AbstractOne):

    def calculateFreqs(self):
        super().calculateFreqs()
        cr = Counter(self.address)

        with open("weirdWords.txt") as f:
            for line in f:
                val = line.split()
                z = []
                for i in val:
                    for j in i:
                        z.append(j)
                        ctr = Counter(z)
                print(ctr)





    def __init__(self, address):
        super().__init__(address)


class DictCount(AbstractOne):

     def calculateFreqs(self):
        super().calculateFreqs()
        with open("weirdWords.txt") as f:
            for line in f:
                val = line.split()
                z = []
                for i in val:
                    z.append(i)

        dictfreqs = {}
        k = 0
        for i in z:
            dictfreqs[k] = i
            k = k+1
        v = {}
        l = 0
        for h in dictfreqs:

            for t in dictfreqs[h]:

                v[l] = t
                l= l+1
        aa= v.values()
        bb = Counter(aa)
        print(bb)




     def __init__(self, address):
         super().__init__(address)




