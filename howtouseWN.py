#example how to use Wordnet in python

from nltk.corpus import wordnet as wn

#nltk.download() #install wordnet,wordnet_ic

print 1,wn.synsets('dog'),"\n"

print 2,"verb" ,"\n",  wn.synsets('dog', pos=wn.VERB),"\n"

print 3,"noun" ,"\n", wn.synsets('dog', pos=wn.NOUN),"\n"

print 4,wn.synset('dog.n.01'),"\n"

print 5,"defination" , (wn.synset('dog.n.01').definition()),"\n"

print 6,"example count" , len(wn.synset('dog.n.01').examples()),"\n"
print 7,wn.synset('dog.n.01').examples()[0],"\n"

dog = wn.synset('dog.n.01')
print 8,dog.hypernyms(),"\n"

print 9,"dog's root","\n",dog.root_hypernyms(),"\n"


