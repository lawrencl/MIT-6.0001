##n = 5775
##s = str (n)
##val = 0
##for x in s:
##        val+= int(x)
##        print 'c: '+str(x)
##        print 's: '+str(s)
##        print 'val: '+str(val)

##s = ['a','b','c']
##x = ['b', 'e']
##if s[1]==x[0]:
##        print "correct"
##else:
##        print "wrong"

# Take a sentence and output the letters in alphabetical order
ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sentence = list('THE QUICK RED FOX JUMPS OVER THE LAZY BROWN DOG')
outside = -1
inside = 0
print "len(ABC)", len(ABC)
print "len(sentence)", len(sentence)
print sorted(sentence)
while (outside < len(ABC)-1):
   outside = outside + 1
   inside = 0
   while (inside < len(sentence)):
        if sentence[inside]==ABC[outside]:
            print 'The sentence is:', sentence[inside]
            inside = inside + 1
        else: 
            inside = inside + 1
print 'Good bye!'
