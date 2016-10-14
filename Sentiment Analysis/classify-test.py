from docclass import *

cl = fisherclassifier(getwords)

rarewords = []

#add words from the frequency list only if they do not have the referenced number of occurrences
freq = file('eu.csv')
for line in freq:
	line = re.sub('\n', '', line)
	pieces = line.split(',')
	#int(pieces[1])
	#print type(pieces[1])
	
	if (pieces[1] != '1' and pieces[1]!='30376' and pieces[1]!='4467' and pieces[1]!='4244' and pieces[1]!='4149' and pieces[1]!='4138'):# and pieces[1]!='2677' and pieces[1]!='1637' and pieces[1]!='1551' and pieces[1]!='1689' and pieces[1]!='617' and pieces[1]!='1059' and pieces[1]!='999' and pieces[1]!='5568' and pieces[1]!='1109':
		rarewords.append(pieces[0])
#print rarewords

#train on positive tweets after the 1500th tweet
#go through words. Train the words as positive only if they belong to rarewords set
goodfile = file('eu-good.txt')
count0 = 0
for line in goodfile:
	count0 += 1
	splitter = re.compile('\\W*')
	linewords = [s.lower() for s in splitter.split(line)
             if len(s) > 2 and len(s) < 20]
	if count0 > 1500:
		for elt in linewords:
			if elt in rarewords:
				cl.train(elt, 'P')
goodfile.close()

#train on negative tweets after the 1500th tweet
#go through words. Train the words as positive only if they belong to rarewords set
badfile = file('eu-bad.txt')
count1=0
for line in badfile:
	count1 += 1
	splitter = re.compile('\\W*')
	linewords = [s.lower() for s in splitter.split(line)
			if len(s) > 2 and len(s) < 20]
	if count1 > 1500:
		for elt in linewords:
			if elt in rarewords:
				cl.train(elt, 'N')
badfile.close()

#test the accuracy of classification algorithm by comparing predictions on negative tweets with the negative category
testbad = file('eu-bad.txt')
count2 = 0
ncount = 0.0
for line in testbad:
	count2 += 1
	result = cl.classify(line)
	if count2 < 1500:
		if(result=='N'):
			ncount += 1		
navg=ncount/1500.0
print 'N success rate: ', navg
testbad.close()

#test the accuracy of classification algorithm by comparing predictions on negative tweets with the negative category
testgood = file('eu-good.txt')
count3 = 0
pcount = 0.0
for line in testgood:
	count3 += 1
	if count3 < 1500:
		if(cl.classify(line)=='P'):
			pcount += 1.0
pavg=pcount/1500.0
print 'P success rate: ', pavg
testgood.close()

#print average correct-ness
print 'Average: ', (pavg+navg)/2.0
