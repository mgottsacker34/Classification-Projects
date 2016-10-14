#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classify.py
#  
#  Copyright 2015 Matthew <Matthew@GISELLE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from docclass import *
import csv 

cl = naivebayes(getwords)

twain1 = file('twain/huckfinn-t.txt')
count=0
for line in twain1:
	count+=1
	if count>551 and count < 10051:
		cl.train(line, 'Mark Twain')
twain1.close()

twain2 = file('twain/connecticutyankee-t.txt')
count=0
for line in twain2:
	count+=1
	if count>88 and count < 10088:
		cl.train(line, 'Mark Twain')
twain2.close()

dickens1 = file('dickens/olivertwist.txt')
count=0
for line in dickens1:
	count+=1
	if count>153 and count < 10153:
		cl.train(line, 'Charles Dickens')
dickens1.close()

dickens2 = file('dickens/greatexpectations.txt')
count=0
for line in dickens2:
	count+=1
	if count>46 and count < 10046:
		cl.train(line, 'Charles Dickens')
dickens2.close()

fitz1 = file('fitzgerald/damned.txt')
count=0
for line in fitz1:
	count+=1
	if count>157 and count < 10157:
		cl.train(line, 'F. Scott Fitzgerald')
fitz1.close()

fitz2 = file('fitzgerald/jazz.txt')
count=0
for line in fitz2:
	count+=1
	if count>249 and count < 10249:
		cl.train(line, 'F. Scott Fitzgerald')
fitz2.close()

poe1 = file('poe/works1.txt')
count=0
for line in poe1:
	count+=1
	if count>2888 and count < 7888:
		cl.train(line, 'Edgar Allen Poe')
poe1.close()

poe2 = file('poe/works2.txt')
count=0
for line in poe2:
	count+=1
	if (count>74 and count < 3454) or (count>4252 and count<9233): #need 5620...4152-9152. 9233
		cl.train(line, 'Edgar Allen Poe')
poe2.close()

poe3 = file('poe/works4.txt')
count=0
for line in poe3:
	count+=1
	if count>73 and count<6712:
		cl.train(line, 'Edgar Allen Poe')
poe3.close()
#need 9000

wilde1 = file('wilde/dorian.txt')
count=0
for line in wilde1:
	count+=1
	if count>96 and count < 8096:
		cl.train(line, 'Oscar Wilde')
wilde1.close()

wilde2 = file('wilde/earnest.txt')
count=0
for line in wilde2:
	count+=1
	if count>99 and count < 3099:
		cl.train(line, 'Oscar Wilde')
wilde2.close()

wilde3 = file('wilde/noimportance.txt')
count=0
for line in wilde3:
	count+=1
	if count>177 and count < 3177:
		cl.train(line, 'Oscar Wilde')
wilde3.close()

wilde4 = file('wilde/ladyfan.txt')
count=0
for line in wilde4:
	count+=1
	if count>189 and count < 2189:
		cl.train(line, 'Oscar Wilde')
wilde4.close()

wilde5 = file('wilde/profundis.txt')
count=0
for line in wilde5:
	count+=1
	if count>45 and count < 1545:
		cl.train(line, 'Oscar Wilde')
wilde5.close()

wilde6 = file('wilde/idealhusband.txt')
count=0
for line in wilde6:
	count+=1
	if count>159 and count < 2659:
		cl.train(line, 'Oscar Wilde')
wilde6.close()

shakes1 = file('shakespeare/allshakespeare.txt')
count=0
for line in shakes1:
	count+=1
	if count>2870 and count < 22870:
		cl.train(line, 'Shakespeare')
shakes1.close()

#Check Twain
f0 = file('twain/lifeonmiss-t.txt')
tocheck=''
count=0
for line in f0:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "Life on the Mississippi" (Twain): ' , cl.classify(tocheck)
f0.close()
#Probability of each category
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''

#Check Dickens
f1 = file('dickens/taleoftwo.txt')
tocheck=''
count=0
for line in f1:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "A Tale of Two Cities" (Dickens): ' , cl.classify(tocheck)
f1.close()
#Probability of each category
print 'Probability it is... '
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''

#Check Fitzgerald
f2 = file('fitzgerald/paradise.txt')
tocheck=''
count=0
for line in f2:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "This Side of Paradise" (F. Scott Fitzgerald):' , cl.classify(tocheck)
f2.close()
#Probability of each category
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''

#Check Poe
f3 = file('poe/usher.txt')
tocheck=''
count=0
for line in f3:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "The Fall of the House of Usher" (Poe): ' , cl.classify(tocheck)
f3.close()
#Probability of each category
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''

#Check Wilde
f4 = file('wilde/happyprince.txt')
tocheck=''
count=0
for line in f4:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "The Happy Prince and Other Tales" (Wilde): ' , cl.classify(tocheck)
f4.close()
#Probability of each category
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''

#Check Shakespeare
f5 = file('shakespeare/macbeth.txt')
tocheck=''
count=0
for line in f5:
	count = count+1
	if count>500 and count<510:
		tocheck += line
print 'Classify "Macbeth" (Shakespeare): ' , cl.classify(tocheck)
f5.close()
#Probability of each category
print 'Probability it is... '
print 'Twain: ', cl.prob(tocheck,'Mark Twain')*100
print 'Dickens: ', cl.prob(tocheck,'Charles Dickens')*100
print 'Fitzgerald: ', cl.prob(tocheck,'F. Scott Fitzgerald')*100
print 'Poe: ', cl.prob(tocheck,'Edgar Allen Poe')*100
print 'Wilde: ', cl.prob(tocheck,'Oscar Wilde')*100
print 'Shakespeare: ', cl.prob(tocheck,'Shakespeare')*100
print ''
