import random
import Queue

print "soccjs"
print "hi ge-algorithm"

tag_set=["friend","airport","birthday","graduation",
         "mom","university","cake","family","trip",
         "vacation","school","food","coffee","flight",
         "interview","restaurant"
         ]

#print tag_set
total_len = len(tag_set)
print total_len 

q = Queue.Queue()
q.put(tag_set)

while True:
    C = q.get()
    A = Queue.Queue()
    B = Queue.Queue()
    
    split_n = random.randint(1, total_len-1)
    print "split_n" , split_n

    for i in range(0,split_n):
        word = random.choice(C)
        C.remove(word)
        A.put(word)
    for i in range(0,total_len-split_n):
        word = random.choice(C)
        C.remove(word)
        B.put(word)
        
    
    
    print A.qsize(), B.qsize(), len(C)
    break    
