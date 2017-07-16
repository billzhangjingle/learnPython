#!/usr/bin/python

def test_fun(n):
	a,b,c = 0,1,0
	while c<n:
		a,b = b, a+b
		c = c + 1
		print b

test_fun(5)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = a, a + b
		n = n + 1

fib(5)

N = ['Hello', 'World', 18, 'Apple', 'None']
hh = (s.lower() for s in N if isinstance(s,str) ==True)
print hh
for item in hh:
	print item
#print hh.next()
#print hh.next()
#print hh.next()
#print hh.next()

#def generator_yield(max):
def create_counter(n):
    print "create counter"
    #while True:
    while False:
        yield n
        print 'increment n'
        n += 1

cnt = create_counter(2)
print cnt
for item in cnt:
	print item
#print next(cnt)
#print next(cnt)
#print cnt.next()
#print cnt.next()	

