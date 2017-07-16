#!/usr/bin/python

classmates=['hello', 'zhang', 'jingle','feiailing']

print classmates
classmates.insert(1, 'jingledddddd')
print classmates
#print classmates[5]
print len(classmates)

sum=0
for x in range(100):
	sum= sum + x
print sum

age = raw_input('age:')
if age >200:
	print "bigger than 200"
else:
	print "small than 200"

def myprint():
	print "maindddddd"

myprint()
