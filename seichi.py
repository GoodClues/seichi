# -*- coding: utf-8 -*-
"""
@author: GoodClues
"""

import csv
import collections

### function ###

# word_array: word array
# lank_num: lanking number
def printLanking(word_array, lank_num):
    count_array = collections.Counter(word_array)
    lank = 1
    for t in count_array.most_common(lank_num):
        print lank, ":", t[1], t[0]
        lank = lank + 1

# word_array: word array
# end_num: end number
def createEndWordArray(word_array, end_num):
    end_word = []
    for wa in word_array:
        end_word.append(wa.decode('utf-8')[-end_num:])
    return end_word

### Setup ###

title = []
seichi = []
prefecture = []

# read csv file
csvReader = csv.reader(open('seichi.csv', 'r'), delimiter=',')
for row in csvReader:
    title.append(row[1])
    seichi.append(row[3])
    prefecture.append(row[4])

### Main ###

print "\n--Title Lanking--"
printLanking(title, 10)

print "\n--Seichi Lanking--"
printLanking(seichi, 10)

print "\n--Prefecture Lanking--"
printLanking(prefecture, 10)
    
print "\n--End 1 word Lanking--"
printLanking(createEndWordArray(seichi, 1), 10)

print "\n--End 2 word Lanking--"
printLanking(createEndWordArray(seichi, 2), 10)

print "\n--End 3 word Lanking--"
printLanking(createEndWordArray(seichi, 3), 10)
