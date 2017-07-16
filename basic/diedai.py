#!/usr/bin/python
d={'a':1,'b':2, 'c':3, 'd':5}
print d
for key in d:
	print key
for value in d.itervalues():
	print value


for key,val in d.iteritems():
	print key,val

for i, value in enumerate(['A', 'B', 'C']):
	 print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y

list=[1,2,3,4,5,6,7,8]

for i,value in enumerate(list):
	print i,value

L = ['Hello', 'World',  'Apple', 'None']
m = [s.lower() for s in L]
print m

N = ['Hello', 'World', 18, 'Apple', 'None']
hh = [s.lower() for s in N if isinstance(s,str) ==True]
print hh

