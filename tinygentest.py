__author__ = 'damariei'

from thing import Thing
from utils import genSeq

	
# Testing
t1 = Thing()
t1.construct(genSeq())
print('T1: '+t1.name)

t2 = Thing()
t2.construct(genSeq())
print('T2: '+t2.name)

print("Diff: "+str(t1.compareTo(t2.seq)))