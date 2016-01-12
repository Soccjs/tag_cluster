#jcn_similarity test
from nltk.corpus import wordnet
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis

brown_ic = wordnet_ic.ic('ic-brown.dat')
genesis_ic = wordnet.ic(genesis,False,0.0)
semcor_ic = wordnet_ic.ic('ic-semcor.dat')



list1 = ['flight']
list2 = ['trip']
list3 = []
for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1,pos=wordnet.NOUN)
        wordFromList2 = wordnet.synsets(word2,pos=wordnet.NOUN)
        print wordFromList1 ,"\n", wordFromList2
        if wordFromList1 and wordFromList2:
            for item1 in wordFromList1:
                for item2 in wordFromList2:
                    s=item1.jcn_similarity(item2,brown_ic)
                    print(item1, item2, s)
                    list3.append(s)

print(max(list3))

print list3
