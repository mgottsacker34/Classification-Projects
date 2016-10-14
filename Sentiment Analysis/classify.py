from docclass import *

cl = fisherclassifier(getwords)

rarewords = []

#read in frequency list
#if the word does not appear once or as many times as listed, add the word to list of words to be tested with test data
freq = file('eu.csv')
for line in freq:
	line = re.sub('\n', '', line)
	pieces = line.split(',')
	#int(pieces[1])
	#print type(pieces[1])
	
	if (pieces[1] != '1' and pieces[1]!='30376' and pieces[1]!='4479' and pieces[1]!='4467' and pieces[1]!='4244' and pieces[1]!='4149' and pieces[1]!='4138'):
		rarewords.append(pieces[0])

#print rarewords

#read in file with positive tweets and train classifier
goodfile = file('eu-good.txt')
for line in goodfile:
	splitter = re.compile('\\W*')
	linewords = [s.lower() for s in splitter.split(line)
             if len(s) > 2 and len(s) < 20]
	for elt in linewords:
		if elt in rarewords:
			cl.train(elt, 'P')
goodfile.close()

#read in file with negative tweets and train classifier
badfile = file('eu-bad.txt')
for line in badfile:
	splitter = re.compile('\\W*')
	linewords = [s.lower() for s in splitter.split(line)
             if len(s) > 2 and len(s) < 20]
	for elt in linewords:
		if elt in rarewords:
			cl.train(elt, 'N')
badfile.close()

#read in test data, classify it, print result
testfile = file('eu-test-dist.txt')
print 'TweetId,Sentiment'
for line in testfile:
	pieces = line.split('\t')
	print pieces[0]+','+cl.classify(pieces[1])
		
